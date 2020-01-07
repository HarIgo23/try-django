from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import BlogPostForm, BlogPostModelForm
from .models import BlogPost


# get -> 1 object
# filter -> [] objects

# CRUD
# GET -> Retrieve / List
# POST -> Create / Update / Delete
# Create Retrieve Update Delete


def blog_post_list_view(request):
    # list out objects
    # could be search

    # filter no publish posts
    # now = timezone.now()
    # qs = BlogPost.objects.filter(publish_data__lte=now)

    qs = BlogPost.objects.published()  # BlogPostManager->publish
    # qs = BlogPost.objects.all().published()  # BlogPostManager->BlogPostQuerySet->publish
    if request.user.is_authenticated:
        my_qs = BlogPost.objects.filter(user=request.user)
        qs = (qs | my_qs).distinct()
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


# @login_required
# The user who have status staff member in admin panel
@staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use a form
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    # if we don't use decorators
    # another way solve problem with anonymous user use:
    # if not request.user.is_authenticated:
    #     return render(request, "not-a-user.html", {})
    if form.is_valid():
        # form.save()
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form': form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # retrieve
    # 1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    template_name = 'form.html'
    context = {"form": form, "title": f"Update{obj.title}"}
    return render(request, template_name, context)


@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('blog_post_list_view')
    context = {'object': obj}
    return render(request, template_name, context)


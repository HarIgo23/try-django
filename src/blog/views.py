from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404

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
    qs = BlogPost.objects.all()  # queryset -> list of python object
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


# @login_required
# The user who have status staff member in admin panel
@staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use a form
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        # obj = form.save(commit=False)
        # some modification to obj
        # obj.save()
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


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {'object': obj}
    return render(request, template_name, context)


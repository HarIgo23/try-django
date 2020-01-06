from django.http import Http404
from django.shortcuts import render, get_object_or_404

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


def blog_post_create_view(request):
    # create objects
    # ? use a form
    template_name = 'blog/create.html'
    context = {'form': None}
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


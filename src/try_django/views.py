from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    my_title = "Hello there...."
    return render(request, "home.html", {"title": my_title, "my_list": [1, 2, 3]})


def about_page(request):
    return render(request, "about.html", {"title": "About Us!"})


def contact_page(request):
    return render(request, "hello_world.html", {"title": "Contact Us"})


def example_page(request):
    my_title = "Hello there...."
    context = {"title": my_title}
    template_name = "title.txt"
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    return render(request, "hello_world.html", {"title": rendered_string})

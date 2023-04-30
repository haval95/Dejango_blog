from django.shortcuts import render
from .models import Post
from django.views import generic


class BlogView(generic.DetailView):
    model = Post
    template_name = "blog.html"


class AboutViwe (generic.TemplateView):
    template_name = "about.html"
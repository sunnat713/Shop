from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class PostsListView(ListView):
    queryset = PostModel.objects.order_by('-pk')
    template_name = 'blog.html'


class PostDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel

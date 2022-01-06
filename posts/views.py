from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


class PostsListView(ListView):
    template_name = 'blog.html'

    def get_queryset(self):
        qs = PostModel.objects.order_by('-pk')
        tag = self.request.GET.get('tag')
        if tag:
            qs = qs.filter(tags__title=tag)
        return qs


class PostDetailView(DetailView):
    template_name = 'blog-details.html'
    model = PostModel

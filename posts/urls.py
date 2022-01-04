from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('', PostsListView.as_view(), name='list')
]

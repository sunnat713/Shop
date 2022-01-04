from django.urls import path

from .views import *

app_name = 'products'
urlpatterns = [
    path('<int:pk>/', ProductsDetailView.as_view(), name='detail'),
    path('', ProductsListView.as_view(), name='list')
]

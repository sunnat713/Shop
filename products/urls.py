from django.urls import path

from .views import *

app_name = 'products'
urlpatterns = [
    path('<int:pk>/', ProductsDetailView.as_view(), name='detail'),
    path('izb/', IzbListView.as_view(), name='izb'),
    path('izb/<int:pk>/', add_izb, name='add-izb'),
    path('', ProductsListView.as_view(), name='list')
]

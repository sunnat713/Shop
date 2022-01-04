from django.urls import path

from .views import *

app_name = 'pages'
urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
]
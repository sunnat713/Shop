from django.urls import path, include
from .views import *

urlpatterns = [
    path('password/change/done/', password_change),
    path('', include('registration.backends.default.urls'))
]

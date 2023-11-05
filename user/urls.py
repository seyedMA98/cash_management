from django.urls import path
from .views import *

urlpatterns = [
    path('register/', user_registration, name='user-registration'),
    path('login/', user_login, name='user-login'),
]

from django.urls import path
from django.contrib import admin

from . import views

app_name='Resume'
urlpatterns = [
    path(r'Resume', views.home, name='home'),
]

from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('<str:category>/',
         views.PostFilter.as_view(),
         name="post_filter"),
]

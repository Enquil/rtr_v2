from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('post_filter/<str:category>/',
         views.PostFilter.as_view(),
         name="post_filter"),
]
# Create your views here.

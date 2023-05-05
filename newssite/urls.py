from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="index"),
    # path('create_post/', views.CreatePost.as_view(), name='create_post'),
    # path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

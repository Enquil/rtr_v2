from django.urls import path
from . import views
from django.views import View
from django.http import (HttpResponse,
                         HttpResponseRedirect)


urlpatterns = [
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]

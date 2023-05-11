from newssite.models import Post
from django.views import View
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)


class PostFilter(View):

    model = Post

    def get(self, request, *args, **kwargs):

        category_filter = self.kwargs.get('category')
        queryset = Post.objects.filter(category=category_filter)

        return render(
            request,
            "post_filter/post_filter.html",
            {
                "post_list": queryset,
            },
        )

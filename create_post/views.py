from django.views import View
from django.shortcuts import render
from newssite.models import Post
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)


class CreatePost(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "create_post/create_post.html",
            {
                # "post_form": PostForm()
            },
        )

    def post(self, request, *args, **kwargs):

        if request.method == "POST":
            post_form = PostForm(request.POST, request.FILES)

            if post_form.is_valid():
                user = User.objects.get(id=request.user.id)
                post_form.instance.email = request.user.email
                post_form.instance.author = request.user
                post = post_form.save(commit=False)
                post.save()
                return HttpResponseRedirect(
                                            reverse(
                                                    'post_detail',
                                                    args=[post.slug]
                                            ))
            else:
                post_form = PostForm()

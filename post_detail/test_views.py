from django.test import TestCase
from newssite.models import Post
from django.contrib.auth.models import User
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
import requests


class TestPostDetail(TestCase):

    def test_get_post_detail(self):
        user = User.objects.create(username='bob',
                                   is_superuser=True,
                                   password='bobspassword')
        post = Post.objects.create(title='bobspost',
                                   author=user,
                                   content="hi, im bob",
                                   category="general",
                                   slug='bob-is-a-slug')
        post.likes.set(('1'))
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

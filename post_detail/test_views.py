from django.test import TestCase
from newssite.models import Post
from django.contrib.auth.models import User
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
import requests


class Testviews(TestCase):

    def test_get_post_detail(self):
        user = User(username='bob',
                    is_superuser=True,
                    password='bobspassword')
        test = Post(title='bobspost',
                    author=user,
                    content="imbob",
                    category="bobcat",
                    slug='bobisaslug',)
        response = self.client.get(render(
                                   requests,
                                   template_name='post_detail.html'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')

from django.test import TestCase
from newssite.models import Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
import requests


class TestPostDetailView(TestCase):

    def test_get_post_detail_templates(self):
        user = User.objects.create(username='bob',
                                   is_superuser=True,
                                   password='bobspassword')
        post = Post.objects.create(title='bobs post',
                                   author=user,
                                   content="hi, im bob",
                                   category="general",
                                   slug='bobs-post')
        post.likes.set(('1'))
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')

    def test_likes(self):
        user = User.objects.create(username='bob',
                                   is_superuser=True,
                                   password='bobspassword')
        post = Post.objects.create(title='bobs post',
                                   author=user,
                                   content="hi, im bob",
                                   category="general",
                                   slug='bobs-post')
        post.likes.set((''))
        self.assertTrue(post.likes.count() == 0)
        post.likes.add(user)
        self.assertTrue(post.likes.count() == 1)
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')

    def test_remove_likes(self):
        user = User.objects.create(username='bob',
                                   is_superuser=True,
                                   password='bobspassword')
        post = Post.objects.create(title='bobs post',
                                   author=user,
                                   content="hi, im bob",
                                   category="general",
                                   slug='bobs-post')
        post.likes.set(('1'))
        self.assertTrue(post.likes.count() == 1)
        post.likes.remove('1')
        self.assertTrue(post.likes.count() == 0)
        response = self.client.get(reverse('post_detail', args=(post.slug,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail/post_detail.html')

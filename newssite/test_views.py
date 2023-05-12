from django.test import TestCase
from . models import Post, Comment
from django.contrib.auth.models import User


class TestPostList(TestCase):

    def test_get_post_list(self):

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newssite/index.html', 'base.html')

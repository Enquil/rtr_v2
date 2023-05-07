from django.test import TestCase
from . models import Post, Comment
from django.contrib.auth.models import User


class TestPost(TestCase):

    def test_published_defaults_to_one(self):
        user = User.objects.create(username='bob',
                                   is_superuser=True,
                                   password='bobspassword')
        post = Post.objects.create(title='bobs post',
                                   author=user,
                                   content="hi, im bob",
                                   category="general",
                                   slug='bob-is-a-slug')
        self.assertEqual(post.status, 1)


# class TestComment(TestCase):

#     def test

from django.test import TestCase
from . models import Post, Comment, Category
from django.contrib.auth.models import User


class TestPost(TestCase):

    def test_published_defaults_to_one(self):
        category_model = Category.objects.create()
        user = User.objects.create(username='bob',
                                   is_superuser=True,
                                   password='bobspassword')
        post = Post.objects.create(title='bobs post',
                                   author=user,
                                   content="hi, im bob",
                                   category=category_model,
                                   slug='bob-is-a-slug')
        self.assertEqual(post.status, 1)

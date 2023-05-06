from django.test import TestCase
from newssite.models import Post
from django.contrib.auth.models import User


class Testviews(TestCase):

    def test_get_post_detail(self):

        user = User(username='bob', is_superuser=True, password='bobspassword')
        post = Post.objects.create(title='bobs post',
                                   author=user,
                                   )
        response = self.client.get('post_detail')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'rtr_v2/post_detail.html')

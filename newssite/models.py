from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
import random


STATUS = ((0, 'Draft'), (1, 'Published'), (2, 'Disabled'))


# Sourced from Code Institute
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Post(models.Model):
    '''
    - Basic post class sourced from CodeInstitute django tutorial
     with some minor modifications:
        - extended slug to allow title to match other posts
        - "status" is 1: "Published", as default
    '''

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='posts')
    updated_on_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.ForeignKey(Category,
                                 max_length=30,
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=300,
                               blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User,
                                   related_name='likes',
                                   blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    # saves and slugifies the post after user submits the form,
    # Use random int and username to prevent duplicate slugs
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                self.title + str(
                    self.author) + str(
                        random.randint(0, 9999999)))
        return super().save(*args, **kwargs)


class Comment(models.Model):
    '''
    - Basic comment class sourced from CodeInstitute django tutorial
     with some minor modifications:
        - Parents and children to be able to use comments as a "conversation"
        - "Approved" field is set to True by default
    '''
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               on_delete=models.CASCADE,
                               related_name='replies')

    class Meta:
        ordering = ["created_on"]

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

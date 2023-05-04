from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
import random

CATEGORY_CHOICES = [
    ('general', "general"),
    ("business", "business"),
    ("art_entertainment", "art and entertainment"),
    ("finance_economics", "finance and economics"),
    ("politics", "politics"),
    ("science", "science"),
    ("opinions", "opinions"),
    ("ships_giggles", "ships and giggles"),
    ]

STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    '''
    - Basic post class mostly taken from CodeInstitute django tutorial
     with some modifications.
    '''

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
        )
    updated_on_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    category = models.CharField(
        max_length=30, choices=CATEGORY_CHOICES, default='general'
        )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

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

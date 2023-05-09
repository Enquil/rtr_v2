from newssite.models import Post
from django.contrib.auth.models import User
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils.translation import ugettext_lazy as _


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'excerpt',
                  'content', 'featured_image')
        widgets = {
            'content': SummernoteWidget(
                       attrs={'summernote': {
                                             'width': '100%',
                                             'height': '400px'
                                            }}),
        }
        labels = {
            'featured_image': 'Select an image'
        }

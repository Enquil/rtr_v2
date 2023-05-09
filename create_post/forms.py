from newssite.models import Post
from django.contrib.auth.models import User
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'category', 'excerpt', 'content', 'featured_image')
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
        # helper = FormHelper()
        # helper.form_class = 'form-group'
        # helper.layout = (
        #     Field('title', css_class='fs-1'),
        #     Field('text', rows="3", css_class='form-control mb-3'),
        #     Field('author', css_class='form-control mb-3'),
        #     Field('tags', css_class='form-control mb-3'),
        #     Field('slug', css_class='form-control'),
        # )

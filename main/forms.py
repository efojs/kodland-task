from django import forms
from .models import BlogPost

from django.utils.text import slugify
from unidecode import unidecode

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'image']

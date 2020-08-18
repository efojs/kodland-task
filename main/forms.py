from django import forms
from django.utils.text import slugify

from unidecode import unidecode

from .models import BlogPost
from .widgets import FileInputWithPreview



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'image']
        widgets = {
            'image': FileInputWithPreview,
        }

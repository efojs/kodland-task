from django import forms
from django.utils.text import slugify

from unidecode import unidecode

from .models import BlogPost
from .widgets import FileInputWithPreview



class BlogPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(placeholder='Введите название статьи')

    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'image']
        widgets = {
            'image': FileInputWithPreview,
        }

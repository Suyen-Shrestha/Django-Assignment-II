from django import forms
from .models import BlogArticle


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model= BlogArticle
        fields = ['title', 'description', 'image']

from django import forms
from .models import Post
from django_summernote.widgets import *


class PostForm(forms.ModelForm): 
    class Meta: # meta class is a class who's instances are classes
        model = Post
        fields = ('post_title', 'post_author', 'post_blurb', 'distance', 'body',)

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_blurb': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 5, 'type': 'number',}),
            'post_author': forms.Select(attrs={'class': 'form-control'}),
            'body': SummernoteWidget(),
        }
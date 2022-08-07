from django import forms
from .models import Post, Profile, Comment
from django_summernote.widgets import *


class PostForm(forms.ModelForm): 
    class Meta: # meta class is a class who's instances are classes
        model = Post
        fields = ('post_title', 'post_blurb', 'header_image', 'distance', 'body',)

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_blurb': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 5, 'type': 'number',}),
            'body': SummernoteWidget(),
        }

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('body',)


class ProfileForm(forms.ModelForm): 
    class Meta: 
        model = Profile
        fields = ('profile_picture',)
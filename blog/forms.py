from django import forms
from .models import Post, Profile, Comment
from django_summernote.widgets import *


class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post
        fields = ('post_title', 'post_blurb', 'header_image', 'image_2', 'image_3', 'distance', 'meters_climbed', 'first_cairn', 'second_cairn', 'third_cairn',  'body',)

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_blurb': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 5, 'type': 'number',}),
            'meters_climbed': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 5, 'type': 'number',}),
            'first_cairn': forms.Select(attrs={'class': 'form-control'}),
            'second_cairn': forms.Select(attrs={'class': 'form-control'}),
            'third_cairn': forms.Select(attrs={'class': 'form-control'}),
            'body': SummernoteWidget({ 'class': '.summernote'}),
        }

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': SummernoteWidget(),
        }

class ProfileForm(forms.ModelForm): 
    class Meta: 
        model = Profile
        fields = ('display_name', 'profile_picture', 'instagram_url', 'strava_url', 'linkedin_url',)

        widgets = {
        'display_name': forms.TextInput(attrs={'class': 'form-control'}),
        'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        'strava_url': forms.TextInput(attrs={'class': 'form-control'}),
        'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
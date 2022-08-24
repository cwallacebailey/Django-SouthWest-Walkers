from django import forms
from .models import Post, Profile, Comment
from django_summernote.widgets import *
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post
        fields = ('post_title', 'header_image', 'image_2', 'image_3', 'distance', 'meters_climbed', 'first_cairn', 'second_cairn', 'third_cairn',  'notes',)

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 5, 'type': 'number',}),
            'meters_climbed': forms.NumberInput(attrs={'minlength': 1, 'maxlength': 5, 'type': 'number',}),
            'first_cairn': forms.Select(attrs={'class': 'form-control', 'id': 'firstCairnForm'}),
            'second_cairn': forms.Select(attrs={'class': 'form-control', 'id': 'secondCairnForm'}),
            'third_cairn': forms.Select(attrs={'class': 'form-control', 'id': 'thirdCairnForm'}),
            'notes': forms.Textarea(attrs={'cols': 30, 'rows' : 5, 'title': 'Notes'}),
        }

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {
            'body': forms.Textarea(attrs={'size': 30, 'rows' : 5,}),
        }

class ProfileForm(forms.ModelForm): 
    class Meta: 
        model = Profile
        fields = ('display_name', 'profile_picture', 'instagram_url', 'strava_url', 'linkedin_url',)

        widgets = {
        'display_name': forms.TextInput(attrs={'class': 'form-control'}),
        'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://www.instagram.com/...', 'pattern': "https://www.instagram.com/*"}),
        'strava_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://www.strava.com/...', 'pattern': "https://www.strava.com/*"}),
        'linkedin_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://www.linkedin.com/...', 'pattern': "https://www.linkedin.com/*"}),
        }
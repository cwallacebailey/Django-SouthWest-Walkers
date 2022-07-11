from django import forms
from .models import Post

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post
        fields = ('post_title', 'post_author', 'body', 'header_image', 'starred', 'slug')

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'required': False,'class': 'form-control','enctype': 'multipart/form-data'}),
            'starred': forms.Select(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
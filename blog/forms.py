from django import forms
from .models import Post

class PostForm(forms.ModelForm): 
    class Meta: 
        model = Post
        fields - (__all__)

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_author': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.TextInput(attrs={'class': 'form-control'}),
            'starred': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
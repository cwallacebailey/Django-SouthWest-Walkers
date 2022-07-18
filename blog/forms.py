from django import forms
from .models import Post

regions = [('Bristol', 'Bristol'), ('The Mendips','The Mendips'), ('The Brecons','The Brecons')]

class PostForm(forms.ModelForm): 
    class Meta: # meta class is a class who's instances are classes
        model = Post
        fields = ('post_title', 'post_author', 'post_region', 'body', 'slug')

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_author': forms.Select(attrs={'class': 'form-control'}),
            'post_region': forms.Select(choices=regions, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }
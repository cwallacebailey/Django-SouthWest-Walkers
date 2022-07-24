from django import forms
from .models import Post

class PostForm(forms.ModelForm): 
    class Meta: # meta class is a class who's instances are classes
        model = Post
        fields = ('post_title', 'post_author', 'body',)

        widgets = {
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
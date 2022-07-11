from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class Home(ListView):
    model = Post
    template_name = 'home.html'

class DetailView(DetailView):
    model = Post
    template_name = 'detail_view.html'

class NewPost(CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'
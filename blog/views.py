from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

class Home(generic.ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 8

class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail_view.html'

class NewPost(generic.CreateView):
    model = Post
    template_name = 'new_post.html'
    fields = '__all__'
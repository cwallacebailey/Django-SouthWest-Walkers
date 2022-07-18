from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy


class Home(generic.ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 8

class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail_view.html'

class NewPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'

class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['post_title', 'post_region', 'body']

class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
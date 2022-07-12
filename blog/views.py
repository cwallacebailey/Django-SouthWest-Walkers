from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import PostForm


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
    fields = ('post_title', 'body', 'slug')
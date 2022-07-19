from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect


# this updates the database using a get object or 404. 

class StarPost(generic.View):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))

        if post.starred.filter(id=request.user.id).exists():
            post.starred.remove(request.user)
        else: 
            post.starred.add(request.user)
        return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class Home(generic.ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 8

class DetailView(generic.DetailView):
    model = Post
    template_name = 'detail_view.html'
    starred = False
    def starred():
        if post.likes.filter(id=self.request.user.id).exists():
            starred = True

class NewPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'
    success_url = reverse_lazy('home')

class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ['post_title', 'body']
    success_url = reverse_lazy('home')

class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


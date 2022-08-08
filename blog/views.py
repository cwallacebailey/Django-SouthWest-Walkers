from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Post, Profile
from .forms import PostForm, ProfileForm, CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from allauth.account.views import SignupView


class Home(generic.ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 8

class DetailView(generic.DetailView):
    def get(self, request, pk, *args, **kwargs):
        queryset = Post.objects
        obj = get_object_or_404(queryset, pk=pk)
        comments = obj.comment.order_by("-created_date")
        return render(
            request,
            "detail_view.html",
            {
                "post": obj,
                "comments": comments,
                "comment_form": CommentForm()
            }
        )
    
    def post(self, request, pk, *args, **kwargs):
        queryset = Post.objects
        obj = get_object_or_404(queryset, pk=pk)
        comments = obj.comment.order_by("-created_date")
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.comment_author = self.request.user
            comment = comment_form.save(commit=False)
            comment.Post = obj
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "detail_view.html",
            {
                "post": obj,
                "comments": comments,
                "comment_form": comment_form
            }
        )

class StarPost(generic.View):
    def post(self, request, pk):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))

        if post.starred.filter(id=request.user.id).exists():
            post.starred.remove(request.user)
        else: 
            post.starred.add(request.user)
        return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class NewPost(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("detail", kwargs={"pk": pk})

class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


# Profile Section Below 


class ProfileView(generic.DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_profile(self, *args, **kwargs):
            users = Profile.objects
            context = super(ProfileView, self).get_context_data(**kwargs) 
            page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
            context["page_user"] = page_user
            return context
    
class CreateProfile(generic.CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateProfile(generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.pk

class CustomSignupView(SignupView):
    success_url = reverse_lazy('create_profile')

# Code below is from this source - https://studygyaan.com/django/django-custom-404-error-template-page

def error_404(request, exception):
    """"
    HTTP 404 errors - diverts to user
    friendly page
    """

    return render(request, 'templates/errors/404.html')

def error_500(request,):
    """"
    HTTP 500 errors - diverts to user
    friendly page
    """

    return render(request, 'templates/errors/500.html')
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from .models import Post, Profile, Comment
from .forms import PostForm, ProfileForm, CommentForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from allauth.account.views import SignupView
from django.core.paginator import Paginator


class Home(generic.ListView):
    """
    Builds the home page
    retrieves 8 posts per page
    allows pagination with navbar
    """
    def get(self, request):

        # retrieve object list from Post
        object_list = Post.objects.all()

        # allow pagination 

        pagination = Paginator(Post.objects.all(), 8)
        site_page = request.GET.get('site_page')
        current_page = pagination.get_page(site_page)
        return render (request,
        'index.html', {
            'current_page': current_page,
            'object_list': object_list,
        })

class About(generic.ListView):
    """
    Allows users to see about the website
    """
    model = Post
    template_name = 'about.html'

class PostDetailView(generic.DetailView):
    """
    renders details of the post
    post allows comments to be posted on
    the view and for users to star the post
    """
    def get(self, request, pk, *args, **kwargs):
        """
        Retrieves the detailed post using its
        PK, orders by created date. 
        """
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
        """
        allows comments to be posted on detail
        view. 
        """
        queryset = Post.objects
        obj = get_object_or_404(queryset, pk=pk)
        comments = obj.comment.order_by("-created_date")
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.comment_author = self.request.user
            comment_id = request.POST.get("") 
            parent_obj = None
            parent_id = None
            try:
                parent_id = int(request.POST.get("parent_id")) # https://www.youtube.com/watch?v=KrGQ2Nrz4Dc
            except:
                parent_id = None

            if parent_id:
                parent_qs = Comment.objects.filter(id=parent_id)
                if parent_qs.exists():
                    parent_obj = parent_qs.first()

            comment = comment_form.save(commit=False)
            comment.response = parent_obj
            comment.Post = obj
            comment.save()
            return HttpResponseRedirect(reverse('detail', args=[str(pk)]))
        else:
            comment_form = CommentForm()

        return render(
            request,
            "detail_view.html",
            {
                "post": obj,
                "comments": comments,
                "comment_form": comment_form,
            }
        )

class StarPost(generic.View):
    """
    This is the blogs like function
    """
    def post(self, request, pk):
        post = get_object_or_404(Post, id=request.POST.get('post_id'))

        if post.starred.filter(id=request.user.id).exists():
            post.starred.remove(request.user)
        else: 
            post.starred.add(request.user)
        return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class NewPost(generic.CreateView):
    """
    Allows user to create new post
    takes user as author automatically
    """
    model = Post
    form_class = PostForm
    template_name = 'new_post.html'

    def form_valid(self, form):
        form.instance.post_author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class UpdatePost(generic.UpdateView):
    """
    Allows user to update their post
    sends user back to post once update
    made
    """    
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("detail", kwargs={"pk": pk})

class DeletePost(generic.DeleteView):
    """
    Allows user to delete posts
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

# Comments Section 

class DeleteComment(generic.DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')

# Profile Section Below 
    
class CreateProfile(generic.CreateView):
    """
    Allows user to create a profile. 
    asigns user to the profile automatically
    """
    model = Profile
    form_class = ProfileForm
    template_name = 'create_profile.html'
    success_url = reverse_lazy('home')

    # if request.method == 'POST':
    #     if form.instance.instagram_url is not "":
    #         if "https://www.instagram.com/" not in str(form.instance.instagram_url):

    #         else: 
    #             form = ProfileForm()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileView(generic.DetailView):
    """
    builds the user profile
    paginates journeys by 8
    adds an array to allow
    awards to be shown
    """
    def get(self, request, pk, *args, **kwargs):
        # retrieves users posts
        queryset = Profile.objects
        obj = get_object_or_404(queryset, pk=request.user.profile.pk)
        user_posts = Post.objects.filter(post_author=request.user)

        # builds pagination
        pagination = Paginator(user_posts, 6)
        site_page = request.GET.get('site_page')
        current_page = pagination.get_page(site_page)

        # array for awards and achievements
        mountain_array = ['Pen y Fan', 'Corn Du', 'Fan y Big', 'Fan Brycheiniog', 'Pen Cerrig Calch', 'Picws Du', 'Fan Frynych', 'Cribyn', 'Mynydd Llangorse', 'Skirrid Fawr', 'Waun Fach', 'Twmpa', 'Mynydd Troed', 'The Blorenge', 'ay Bluff', 'Pen Y Gadair Fawr', 'Sugar Loaf', 'Fan Fawr', 'Crug Hywel', 'Tor Y Foel']
        
        # calculate number of peaks reached and which peaks have been climbed
        mountains_walked = []

        for posts in user_posts:
            if posts.first_cairn in mountains_walked:
                pass
            elif posts.first_cairn is None or posts.first_cairn == '':
                pass
            else: 
                mountains_walked.append(posts.first_cairn)
                mountain_array.remove(posts.first_cairn)

        for posts in user_posts:
            if posts.second_cairn in mountains_walked:
                pass
            elif posts.second_cairn is None or posts.second_cairn == '':
                pass
            else: 
                mountains_walked.append(posts.second_cairn)
                mountain_array.remove(posts.second_cairn)
                
        for posts in user_posts:
            if posts.third_cairn in mountains_walked:
                pass
            elif posts.third_cairn is None or posts.third_cairn == '':
                pass
            else: 
                mountains_walked.append(posts.third_cairn)
                mountain_array.remove(posts.third_cairn)

        peaks_reached = len(mountains_walked)


        # get total distance walked
        distance = 0
        for posts in user_posts:
            distance += posts.distance

        return render(
            request,
            "profile.html",
            {            
                "profile": obj,
                "current_page": current_page,
                "distance": distance,
                "mountain_array": mountain_array,
                "mountains_walked": mountains_walked,
                "peaks_reached": peaks_reached
            }
        )

class UpdateProfile(generic.UpdateView):
    """
    Allows user to update their profile
    details
    """
    model = Profile
    template_name = 'update_profile.html'
    form_class = ProfileForm

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("profile", kwargs={"pk": pk})

class CustomSignupView(SignupView):
    """
    User automatically taken to 
    create profile upon signing up
    instead of home page
    """
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
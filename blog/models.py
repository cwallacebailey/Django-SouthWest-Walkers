from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


class Post(models.Model):
    post_title = models.CharField(max_length=150, unique=True)
    post_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    post_blurb = models.CharField(max_length=100)
    distance = models.FloatField()
    body = models.TextField()
    header_image = CloudinaryField('image', default='placeholder', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) # updates the date instead of creating it anew
    starred = models.ManyToManyField(
        User, blank=True)
    
    def total_stars(self):
        return self.starred.count()

    class Meta: 
        ordering = ['-created_date', 'post_author'] # descending order then by author
    
    def __str__(self):
        return self.post_title + ' | ' + str(self.post_author)

    def get_absolute_url(self):
        return reverse('detail', args=(str(self.id))) # this will go to the post just created using its id - replaced by reverse_lazy to home. WASN'T WORKING NEEDS REVIEW.


class Comment(models.Model):
    Post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment"
    )
    comment_author = models.CharField(max_length=70)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) # updates the date instead of creating it anew

    class Meta: 
        ordering = ['-created_date']

    def __str__(self):
        return self.str(comment_author) + ' : ' + self.body


class ProfilePicture(models.Model):
    user_name = models.CharField(max_length=150, unique=True)
    profile_image = CloudinaryField('image', default='placeholder', null=True, blank=True)

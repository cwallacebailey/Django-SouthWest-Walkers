from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    post_title = models.CharField(max_length=150, unique=True)
    post_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    body = models.TextField()
    header_image = CloudinaryField('image', default='placeholder')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    starred = models.ManyToManyField(
        User, blank=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta: 
        ordering = ['-created_date', 'post_author'] # descending order then by author
    
    def __str__(self):
        return self.post_title + ' | ' + str(self.post_author)

    def number_of_times_starred(self):
        return self.starred.count()


class Comment(models.Model):
    Post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment"
    )
    comment_author = models.CharField(max_length=70)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta: 
        ordering = ['-created_date']

    def __str__(self):
        return self.str(comment_author) + ' : ' + self.body
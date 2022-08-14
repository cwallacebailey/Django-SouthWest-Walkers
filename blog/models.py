from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

cairn_choices = (
    ('Pen y Fan', 'Pen y Fan'),
    ('Corn Du', 'Corn Du'),
    ('Fan y Big', 'Fan y Big'),
    ('Fan Brycheiniog', 'Fan Brycheiniog'),
    ('Pen Cerrig Calch', 'Pen Cerrig Calch'),
    ('Picws Du', 'Picws Du'),
    ('Fan Frynych', 'Fan Frynych'),
    ('Cribyn', 'Cribyn'),
    ('Mynydd Llangorse', 'Mynydd Llangorse'),
    ('Skirrid Fawr', 'Skirrid Fawr'),
    ('Waun Fach', 'Waun Fach'),
    ('Twmpa', 'Twmpa'),
    ('Mynydd Troed', 'Mynydd Troed'),
    ('The Blorenge', 'The Blorenge'),
    ('ay Bluff', 'ay Bluff'),
    ('Pen Y Gadair Fawr', 'Pen Y Gadair Fawr'),
    ('Sugar Loaf', 'Sugar Loaf'),
    ('Fan Fawr', 'Fan Fawr'),
    ('Crug Hywel', 'Crug Hywel'),
    ('Tor Y Foel', 'Tor Y Foel'),
)

class Post(models.Model):

    post_title = models.CharField(max_length=150, unique=True)
    post_author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    post_blurb = models.CharField(max_length=100, null=True)
    distance = models.FloatField()
    meters_climbed = models.FloatField(default=0, null=True)
    body = models.TextField()
    header_image = CloudinaryField('image', default='placeholder', null=True, blank=True)
    image_2 = CloudinaryField('image', default='placeholder', null=True, blank=True)
    image_3 = CloudinaryField('image', default='placeholder', null=True, blank=True)
    first_cairn = models.CharField(max_length = 20, choices = cairn_choices , default = '', null=True, blank='true')
    second_cairn = models.CharField(max_length = 20, choices = cairn_choices , default = '', null=True, blank='true')
    third_cairn = models.CharField(max_length = 20, choices = cairn_choices , default = '', null=True, blank='true')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) # updates the date instead of creating it anew
    starred = models.ManyToManyField(
        User, blank=True)

    
    def total_stars(self):
        return self.starred.count()

    class Meta: 
        ordering = ['-created_date', 'post_author']
    
    def __str__(self):
        return self.post_title + ' | ' + str(self.post_author)

    def get_absolute_url(self):
        return reverse('detail', args=(str(self.id)))


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile"
    )
    display_name = models.CharField(max_length=150, unique=True,)
    profile_picture = CloudinaryField('image', default='placeholder', null=True, blank=True)
    instagram_url = models.CharField(max_length=150, unique=False, null=True, blank=True, default='',)
    strava_url = models.CharField(max_length=150, unique=False, null=True, blank=True, default='',)
    linkedin_url = models.CharField(max_length=150, unique=False, null=True, blank=True, default='',)

    # def __str__(self):
    #     return str(self.user)

class Comment(models.Model):
    Post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment"
    )
    comment_author = models.CharField(max_length=70)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    response = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)

    class Meta: 
        ordering = ['-created_date']

    def __str__(self):
        return str(self.comment_author) + ' : ' + self.body



from django.contrib import admin
from .models import Post, Profile, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('body')
    list_filter = ('post_title', 'created_date')
    list_display = ('post_title', 'post_author', 'created_date', 'pk')
    search_fields = ('post_title', 'post_author', 'created_date', 'pk')


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('display_name', 'profile_picture', 'user', 'pk')


@admin.register(Comment)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('body', 'comment_author', 'response')

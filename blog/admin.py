from django.contrib import admin
from .models import Post, Profile, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """"
    Allows admin to manage posts data via the admin panel
    """
    summernote_fields = ('body')
    list_filter = ('post_title', 'created_date')
    list_display = ('post_title', 'post_author', 'created_date', 'pk')
    search_fields = ('post_title', 'post_author', 'created_date', 'pk')


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    """"
    Allows admin to manage profile data via the admin panel
    """

    list_display = ('display_name', 'profile_picture', 'user', 'pk')


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """"
    Allows admin to manage profile data via the admin panel
    """

    list_display = ('body', 'comment_author', 'response')

from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('body')
    list_filter = ('post_title', 'created_date')
    list_display = ('post_title', 'post_author', 'created_date', 'pk')
    search_fields = ('post_title', 'post_author', 'created_date', 'pk')
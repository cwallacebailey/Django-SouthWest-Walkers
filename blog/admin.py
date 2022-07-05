from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# we added summernote in the below

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('body')
    prepopulated_fields = {'slug': ('post_title',)}
    list_filter = ('post_title', 'created_date')
    list_display = ('post_title', 'post_author', 'created_date', 'slug')
    search_fields = ('post_title', 'post_author', 'created_date', 'slug')



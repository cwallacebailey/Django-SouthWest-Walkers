from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
]

handler404 = 'blog.views.error_404'
handler500 = 'blog.views.error_500'

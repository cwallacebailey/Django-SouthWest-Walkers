from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('add_post/', NewPost.as_view(), name='add_post'),
    path('detail/update/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('detail/delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('star_post/<int:pk>', StarPost.as_view(), name='star_post'),
]
from django.urls import path
from .views import Home, DetailView, NewPost

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('add_post/', NewPost.as_view(), name='add_post'),
]
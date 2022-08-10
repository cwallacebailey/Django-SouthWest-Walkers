from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('detail/<int:pk>', PostDetailView.as_view(), name='detail'),
    path('add_post/', NewPost.as_view(), name='add_post'),
    path('detail/update/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('detail/delete/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('star_post/<int:pk>', StarPost.as_view(), name='star_post'),

    # Profile URLs below: 
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/update_profile/<int:pk>', UpdateProfile.as_view(), name='update_profile'),
    path('profile/create_profile', CreateProfile.as_view(), name='create_profile'),
]
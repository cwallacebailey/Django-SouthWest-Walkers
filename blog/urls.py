from django.urls import path
from .views import Home, DetailView

urlpatterns = [
    path('', Home.as_view(), name="home")
    path('detail/<int:pk>', DetailView.as_view(), name="detail"),
]
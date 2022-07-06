from django.urls import path
from .views import Home

urlpatterns = [
    path('', HomeView.as_view() name="home")
]
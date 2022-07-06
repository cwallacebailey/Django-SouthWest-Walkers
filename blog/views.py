from django.shortcuts import render
from django.views.generic import ListView, DetailedView

def home(request):
    return render(request, home.html, {})



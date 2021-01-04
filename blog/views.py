from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post
# Create your views here.

class HomeView(ListView):
    template_name = 'home.html'
    model = Post

class DetailedView(DetailView):
    template_name = 'detailed_view.html'
    model = Post
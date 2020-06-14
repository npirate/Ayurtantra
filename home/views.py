from django.shortcuts import render

from django.views.generic import TemplateView #where there is not interaction with model

# Create your views here.

class HomePageView (TemplateView):
    template_name = 'home.html'

class AboutUsView (TemplateView):
    template_name = 'about.html'
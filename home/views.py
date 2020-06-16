from django.shortcuts import render
from providers.models import Provider
from django.views.generic import TemplateView, ListView #where there is no interaction with model

# Create your views here.

class HomePageView (ListView):
    model = Provider
    template_name = 'home.html'
    context_object_name = 'provider_list'

class AboutUsView (TemplateView):
    template_name = 'about.html'
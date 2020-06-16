from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Provider

# Create your views here.

class ProviderListView (ListView):
    model = Provider
    template_name = 'providers/provider_list.html'
    context_object_name = 'provider_list'

class ProviderDetailView (DetailView):
    model = Provider
    template_name = 'providers/provider_detail.html'
    context_object_name = 'provider'
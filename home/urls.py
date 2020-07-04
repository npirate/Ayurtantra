from django.urls import path

from .views import HomePageView, AboutUsView
from providers.views import ProviderDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('<str:pk>/', ProviderDetailView.as_view(), name='provider_profile'),
    path('about/', AboutUsView.as_view(), name = 'about'),
]
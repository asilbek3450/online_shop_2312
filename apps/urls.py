from apps.products.views import HomePageView
from django.urls import path, include



urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
]    
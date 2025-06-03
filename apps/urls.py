from apps.products.views import HomePageView, ShopPageView, ProductDetailView
from django.urls import path, include



urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('shop/', ShopPageView.as_view(), name='shop_page'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='single_product')
]    
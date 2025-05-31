from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Category, ProductImage

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.order_by('-id')[:8]
        return context
    
class ShopPageView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['products'] = Product.objects.filter(available=True).order_by('-id')
        return context
    
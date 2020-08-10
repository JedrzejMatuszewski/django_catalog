from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, ProductGallery

class  ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'product_obj'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        gallery = ProductGallery.objects.filter(product=product)
        context['product_obj'] = product
        context['gallery_obj'] = gallery
        return context
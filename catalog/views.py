from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Product, ProductGallery, Category

from django.core.paginator import Paginator

class  ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'product_obj'
    queryset = Product.objects.all().order_by('title')
    paginate_by = 9


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all().order_by('title')
        context['category_obj'] = categories
        context['title'] = 'Katalog'
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        gallery = ProductGallery.objects.filter(product=product)
        context['product_obj'] = product
        context['gallery_obj'] = gallery
        context['title'] = product.title
        return context


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['title', 'category', 'price', 'sale', 'auction_url', 'img', 'short_description', 'description']
    template_name = 'catalog/product_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edytuj produkt'
        return context

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class ProductCategoryListView(ListView):
    model = Product
    template_name = 'catalog/product_category.html'
    context_object_name = 'product_obj'
    paginate_by = 9


    def get_queryset(self):
        queryset = get_list_or_404(Product,category__slug=self.kwargs['slug'])
        queryset.sort()
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_obj'] = Category.objects.all().order_by('title')
        context['current_cat_slug'] = self.kwargs['slug']
        context['title'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context



def contact(request):
    context = {'title': 'Kontakt'}
    return render(request, 'catalog/contact.html', context)
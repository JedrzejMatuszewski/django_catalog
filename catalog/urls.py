
from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductDetailView, ProductCategoryListView, contact

urlpatterns = [
    path('',ProductListView.as_view(), name='homepage'),
    path('kontakt/', contact, name='contact'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name="product-detail"),
    path('<slug:slug>/', ProductCategoryListView.as_view(), name="product-category"),
]


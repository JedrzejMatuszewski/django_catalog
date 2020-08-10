
from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('',ProductListView.as_view(), name='homepage'),
    path('<slug:slug>/', ProductDetailView.as_view(), name="product-detail"),
]


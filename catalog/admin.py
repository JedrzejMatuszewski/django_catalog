from django.contrib import admin
from .models import Category, Product, ProductGallery

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ProductGalleryAdmin(admin.StackedInline):
    model = ProductGallery

admin.site.register(Category, CategoryAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'price', 'sale', 'auction_url') 
    inlines = [ProductGalleryAdmin]
    
    class Meta:
         model = Product


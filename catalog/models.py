from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
import math

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)    


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    sale = models.IntegerField(default=0)
    auction_url = models.CharField(max_length=200, default="#")
    img = models.ImageField(default='img/default-product-img.jpg', upload_to='img/')
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

    def __gt__(self, other):
        return self.title > other.title

    def show_promo(self):
        return round(100 - (self.sale*100)/self.price)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(default='img/default-product-img.jpg', upload_to='img/')

    def __str__(self):
        return self.product.title

    

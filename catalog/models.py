from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

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
    product_id = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    short_description = models.TextField(default="")
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    img = models.ImageField(default='img/default-product-img.jpg', upload_to='img/')

    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.title

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

    

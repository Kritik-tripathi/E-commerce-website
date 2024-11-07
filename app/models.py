from django.db import models # type: ignore
from django.utils.text import slugify # type: ignore

# Create your models here.
class slider (models.Model):
    image = models.ImageField (upload_to= 'media/slider_imgs')
    Brand = models.CharField (default = "H&M" ,max_length=100)
    Discount = models.IntegerField()
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.Brand
    
class main_category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save (self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Product (models.Model):
    category = models.ForeignKey (main_category, related_name='product', on_delete=models.CASCADE )
    product_name = models.CharField (max_length=100)
    product_info = models.TextField()
    image = models.ImageField(upload_to='media/slider_imgs', default='media/slider_imgs/default.jpg')
    price = models.IntegerField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name
    
class CartItem(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def total_price (self):
        return self.product.price * self.quantity
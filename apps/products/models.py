from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

# Category
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)


# Product
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True, blank=True)
    description = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name.lower())
        self.discount_price = self.price * 0.9
        super().save(*args, **kwargs)

    def get_images(self):
        return ProductImage.objects.filter(product=self)
    
    
    def get_cover_image(self):
        images = self.get_images()
        if images.exists():
            return images[0].image_file.url
    
    def get_reviews(self):
        return Review.objects.filter(product=self).order_by('-created_at')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_file = models.ImageField(upload_to='products/')
    image_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"Image for {self.product.name}"
    
    
# Review
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    RATING = {
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    }
    rating = models.IntegerField(choices=RATING)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} on {self.product.name}"


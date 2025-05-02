from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name

class Shirt(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False) 
    brand = models.CharField(max_length=100, null=False, unique=True) 
    model_name= models.CharField(max_length=100, null=False, unique=True) 
    description = models.TextField(null=False) 
    image = models.ImageField(upload_to='shirts/',blank=True,null=True)
    
    def __str__(self):
        return self.brand
    
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
    
from django.contrib.auth.models import AbstractUser
class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)  # If you have login system
    session_key = models.CharField(max_length=40, null=True, blank=True)  # For guest users
    product = models.ForeignKey('Shirt', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.brand} - {self.quantity}"

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)
#     profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

#     def __str__(self):
#         return self.username


from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):

    PET_TYPES = [
        ('dog', 'Собаки'),
        ('cat', 'Кошки'),
        ('bird', 'Птицы'),
        ('rodent', 'Грызуны'),
        ('fish', 'Рыбы'),
    ]

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    in_stock = models.BooleanField(default=True)
    pet_type = models.CharField(max_length=20, choices=PET_TYPES)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])
    
    class Meta:
        ordering = ['name']
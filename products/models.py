from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from unicodedata import name
from django.db import models


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    image = models.ImageField(upload_to='imges', blank=True)
    actif = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = ('Product')
        verbose_name_plural = ('Products')
        
    def __str__(self):
        return self.name


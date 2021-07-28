from django.db import models

# Create your models here.
class Product(models.Model):

    CATEGORY_CHOICES = (
        ('diy','DIY'),
        ('character inspired', 'Character Inspired'),
        ('caniafe orginals', 'Caniafe Originals')
    )
    
    description = models.TextField()
    image = models.ImageField()
    name = models.CharField(max_length=150)
    price = models.IntegerField() 
    category = models.CharField(max_length=80, choices=CATEGORY_CHOICES, null=True)

    def __str__(self):
        return self.name
from django.contrib import admin
# from rest_framework import serializers
# from rest_framework.relations import HyperlinkedRelatedField
from .models import Product

admin.site.register(Product)

# class ProductSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Product
#         fields = ('description', 'image', 'name', 'price', 'category')

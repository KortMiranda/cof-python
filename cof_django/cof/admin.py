from django.contrib import admin
# from rest_framework import serializers
# from rest_framework.relations import HyperlinkedRelatedField
from .models import Product, Review

admin.site.register(Product)
admin.site.register(Review)



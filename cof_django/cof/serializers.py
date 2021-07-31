from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from .models import Product, Review

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'price', 'category')

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name='product_detail',
        read_only=True
    )

    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product'
    )
    class Meta:
        model = Review
        fields = ('client', 'content', 'product', 'product_id')
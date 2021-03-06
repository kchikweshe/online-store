# import serializer class and models
from rest_framework import serializers

from .models import Product, Category


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'category')


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ('name')

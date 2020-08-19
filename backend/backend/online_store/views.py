# Create your views here.

from rest_framework import viewsets  # add this

from .models import Product, Category  # add this
from .serializers import ProductSerializer, CategorySerializer  # add this


class ProductView(viewsets.ModelViewSet):  # add this
    serializer_class = ProductSerializer  # add this
    queryset = Product.objects.all()  # add this

    def create(self, request, *args, **kwargs):
        pass


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

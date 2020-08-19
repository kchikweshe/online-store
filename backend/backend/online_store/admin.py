from django.contrib import admin

# Register your models here.
from backend.online_store.models import Category, Product

admin.register(Product,Category)
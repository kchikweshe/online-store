from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from backend.online_store import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'products')
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]

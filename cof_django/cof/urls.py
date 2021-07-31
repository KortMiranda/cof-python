from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('products/', views.ProductList.as_view(), name="product_list"),
    path('products/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
]
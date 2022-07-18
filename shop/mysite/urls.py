from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('', IndexView.as_view(), name='home'),
    path('', index, name='home'),
    path('shop/', shop, name='shop'),
    # path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('product/<int:pk>/', product_detail, name='product'),
    path('category/<str:slug>/', product_by_category, name='category'),
    # path('category/<str:slug>/', ProductByCategory.as_view(), name='category'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

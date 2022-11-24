from django.urls import path
from app import views


urlpatterns = [
    path('', views.index),
    path('quotation/', views.quotation, name='quotation'),
    path('products/', views.products, name='products'),
    ]
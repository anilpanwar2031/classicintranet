from django.urls import path
from app import views


urlpatterns = [
    path('', views.index),
    path('quotations/', views.quotation, name='quotations'),
    path('products/', views.products, name='products'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quot/<int:pk>', views.quotdetail, name='quotdetail'),
    ]
from django.urls import path
from app import views


urlpatterns = \
    [
        path('', views.index, name='index'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('quotations/', views.quotation, name='quotations'),
        path('products/', views.products, name='products'),
        # path('quot/<int:pk>', views.quotdetail, name='quotdetail'),
    ]
from django.contrib import admin
from .models import (
 Quotation,
 Product,
 Client,
)

@admin.register(Quotation)
class CustomerModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'quot_no', 'name']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'quantity',  'description']

@admin.register(Client)
class CartModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'surname']



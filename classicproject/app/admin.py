from django.contrib import admin
from .models import (Quotation, Section, Product,
                     Subsection,
                     Client, Quotation_item
                     )
from import_export.admin import ImportExportModelAdmin


@admin.register(Quotation)
class QuotationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'quot_no', 'name']


@admin.register(Section)
class SectionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quotation_id']


@admin.register(Product)
class ProductModelAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'quantity']


@admin.register(Subsection)
class SubsectionectionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section_id']


@admin.register(Client)
class ClientModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname']


@admin.register(Quotation_item)
class Quotation_itemModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'quotation_id', 'subsection_id']



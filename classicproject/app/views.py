from django.shortcuts import render, redirect, HttpResponse
from .models import Quotation, Product
    # , Product, Quotation_item, Client, Section
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')


def dashboard(request):
    quots = Quotation.objects.all().count()
    products = Product.objects.all().count()
    users = User.objects.all().count()
    active = 'dashboard'
    return render(request, "dashboard.html", {"quots": quots, "products": products, "users": users, "active": active})


def quotation(request):
    quots = Quotation.objects.all()
    active = 'quotation'
    return render(request, "quotation.html", {"quots": quots, "active": active})


# def quotdetail(request, pk):
#     quotitem = Quotation_item.objects.get(quotation_id=pk)
#     client = Client.objects.get(quotation_id=pk)
#     sections = Section.objects.filter(quotation_id=pk)
#     return render(request, "quotationdetail.html", {"quotitem": quotitem, "client": client, "sections": sections})
#
#
def products(request):
    prods = Product.objects.all()
    return render(request, "product.html", {"prods": prods})



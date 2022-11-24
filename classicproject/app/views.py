from django.shortcuts import render, redirect, HttpResponse
from .models import Quotation, Product


def index(request):
    return render(request, "home.html",)


def quotation(request):
    quots = Quotation.objects.all()
    return render(request, "quotation.html", {"quots":quots})


def products(request):
    prods = Product.objects.all()
    return render(request, "product.html", {"prods":prods})



from django.shortcuts import render, redirect, HttpResponse
from .models import Quotation, Product, Quotation_item


def index(request):
    return render(request, "home.html",)


def quotation(request):
    quots = Quotation.objects.all()
    return render(request, "quotation.html", {"quots":quots})


def quotdetail(request, pk):
    quot = Quotation_item.objects.get(quotation_id=pk)
    print(quot.subsection_id.name)
    return render(request, "quotationdetail.html", {"quot":quot})


def products(request):
    prods = Product.objects.all()
    return render(request, "product.html", {"prods":prods})



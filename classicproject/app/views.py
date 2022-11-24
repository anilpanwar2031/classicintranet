from django.shortcuts import render, redirect, HttpResponse
from .models import Quotation, Product, Quotation_item, Client, Section


def index(request):
    return render(request, "home.html",)


def quotation(request):
    quots = Quotation.objects.all()
    return render(request, "quotation.html", {"quots":quots})


def quotdetail(request, pk):
    quotitem = Quotation_item.objects.get(quotation_id=pk)
    client = Client.objects.get(quotation_id=pk)
    sections = Section.objects.filter(quotation_id=pk)
    return render(request, "quotationdetail.html", {"quotitem":quotitem, "client":client, "sections":sections})


def products(request):
    prods = Product.objects.all()
    return render(request, "product.html", {"prods":prods})



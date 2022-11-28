from django.shortcuts import render, redirect, HttpResponse
from .models import Quotation, Product, QuotationItem, Section
from django.contrib.auth.models import User



def index(request):
    return render(request, "dashboard.html",)


def dashboard(request):
    quots = Quotation.objects.all().count()
    products = Product.objects.all().count()
    users = User.objects.all().count()

    return render(request, "dashboard.html", {"quots": quots, "products": products, "users": users})


def quotation(request):
    quots = Quotation.objects.all()
    return render(request, "quotation.html", {"quots":quots})


def quotdetail(request, pk):
    quotitem = QuotationItem.objects.get(quotation_id=pk)
    # client = Client.objects.get(quotation_id=pk)
    sections = Section.objects.filter(quotation_id=pk)
    return render(request, "quotationdetail.html", {"quotitem":quotitem, "sections": sections})


def products(request):
    prods = Product.objects.all()
    return render(request, "product.html", {"prods":prods})



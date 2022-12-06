from django.shortcuts import render, redirect, HttpResponse
from .models import Quotation, Product
    # , Product, Quotation_item, Client, Section
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from datetime import datetime
from .models import quotaionstatus


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
    # for q in quots:
    #     print("status", q.get_quot_status_display())
    return render(request, "quotation.html", {"quots": quots})


def quotdetail(request, pk):
    print("pk", pk)
    products = Product.objects.all()
    quot = Quotation.objects.get(id=pk)

    print("quot", quot.name)
    context = {'products': products, 'quot': quot}
    return render(request, "quotationdetail.html", context)
    # quotitem = Quotation_item.objects.get(quotation_id=pk)
    # client = Client.objects.get(quotation_id=pk)
    # sections = Section.objects.filter(quotation_id=pk)
    # return render(request, "quotationdetail.html", {"quotitem": quotitem, "client": client, "sections": sections})
    #


def products(request):
    prods = Product.objects.all()
    return render(request, "product.html", {"prods": prods})


def qsearch(request):
    if request.method == 'POST':
        search = request.POST['search'].lower()
        print("Search = = ", search)

        queryset = Quotation.objects.filter(Q(quot_no__icontains=search) | Q(name__icontains=search) | Q(quot_status__icontains=search) | Q(market_seg__icontains=search))
        data = [{'quot_no': d.quot_no, 'name': d.name, 'quot_status': d.get_quot_status_display(), 'market_seg': d.market_seg,
                 'created_at': d.created_at.strftime("%b %d,%Y") + " | " + d.created_at.strftime("%H:%M %p").lower(), 'created_by': d.created_by.email} for d in queryset]

        for d in queryset:
            print("datetime", d.created_at.strftime("%b %d,%Y") + " | " + d.created_at.strftime("%H:%M %p").lower())
        # print("Data1 = ", data)
        return JsonResponse(data, safe=False)


def psearch(request):
    if request.method == 'POST':
        search = request.POST['search'].lower()
        print("Search = = ", search)

        queryset = Product.objects.filter(Q(name__icontains=search) | Q(description__icontains=search)).values()
        data = list(queryset)
        print("Data = ", data)
        return JsonResponse(data, safe=False)







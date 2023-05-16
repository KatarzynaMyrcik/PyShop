from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
 #   return HttpResponse("hELLO wORLD")
    return render(request, "index.html", {"products": products})

def new_view(request):
    return HttpResponse("new products")


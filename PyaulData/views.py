from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    str = ''
    for p in products:
        str += "{} 상품의 현재수량: {}개 / 판매가능여부: {}<br>".format(
            p.name, p.count, p.usage
        )
        str += p.description + '</p>'

    return HttpResponse(str)
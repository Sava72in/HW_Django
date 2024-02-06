from http.client import HTTPResponse

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    if request.GET.get('sort') == 'name':
        phones = Phone.objects.order_by('name')
    elif request.GET.get('sort') == 'min_price':
        phones = Phone.objects.order_by('price')
    elif request.GET.get('sort') == 'max_price':
        phones = Phone.objects.order_by('-price')
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)




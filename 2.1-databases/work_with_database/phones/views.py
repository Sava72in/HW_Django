from http.client import HTTPResponse

from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    # phone_obj = Phone.objects.all()
    # context = {'phone.price': phone.price for phone in phone_obj}
    # context = {'phone.price': phone.price for phone in Phone.price}
    ob = Phone.objects.all()
    context = {'phone.name':phone.name for phone in ob}
    print(context)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)


def show_test(request):
    template = 'catalog.html'
    phone_obj = Phone.objects.all()
    context = {phone.name for phone in phone_obj}
    print(context)
    return render(request, template, context)
    # return HTTPResponse(context)
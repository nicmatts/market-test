from django.shortcuts import render_to_response, RequestContext, Http404, render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Product, Category

# Create your views here.
def list_all(request):
    products = Product.objects.filter(active=True).order_by('title')
    context = {'products': products}

    return render(request, 'all.html', context)

def single(request):
    product = Product.objects.all()[0]
    context = {'product': product}

    return render(request, 'single.html', context)

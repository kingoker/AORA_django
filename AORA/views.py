from django.shortcuts import render
from .models import *


def index(request):
    mainImages = MainImage.objects.filter(mainPage__isnull=False)
    mainPages = MainPage.objects.all()

    print(mainImages.values())

    context  = {
        'mainImages': mainImages,
        "mainPages": mainPages,
    }

    return render(request, 'index.html', context)


def about(request):
    pass

    return render(request, 'about.html')


def innovation(request):
    innovationPage = InnovationPage.objects.all()
    context  = {
        "innovationPage": innovationPage,
    }

    return render(request, 'innovation.html', context)


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    print("hello world")
    context  = {
        "categories": categories,
        "products": products
    }

    return render(request, 'products.html', context)


def product(request, slug):
    product = Product.objects.filter(slug=slug)

    context  = {
        "product": product
    }

    return render(request, 'product.html', context)


def contacts(request):
    contactsPage = ContactInformation_Page.objects.all()

    context  = {
        'contactsPage': contactsPage
    }

    return render(request, 'contacts.html', context)
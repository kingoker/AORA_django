from django.shortcuts import render
from .models import *
import requests


#Страница Главная
def index(request):
    mainImages = MainImage.objects.filter(mainPage__isnull=False)
    mainPages = MainPage.objects.all()[:1]

    context  = {
        'mainImages': mainImages,
        "mainPages": mainPages,
    }

    return render(request, 'index.html', context)


#Страница О нас
def about(request):
    mainImages = MainImage.objects.filter(aboutPage__isnull=False)[:1]
    differenceItems = DifferenceItem.objects.filter(aboutPage__isnull=False)
    scienceItems = ScienceItem.objects.filter(aboutPage__isnull=False)
    aboutPages = AboutPage.objects.all()[:1]

    context  = {
        'scienceItems': scienceItems,
        'differenceItems': differenceItems,
        'mainImages': mainImages,
        'aboutPages': aboutPages,
    }

    return render(request, 'about.html', context)


#Страница Инноваций
def innovation(request):
    mainImages = MainImage.objects.filter(innovationPage__isnull=False)[:1]
    differenceItems = DifferenceItem.objects.filter(innovationPage__isnull=False)
    innovationPages = InnovationPage.objects.all()[:1]

    context  = {
        'differenceItems': differenceItems,
        'mainImages': mainImages,
        'innovationPages': innovationPages,
    }

    return render(request, 'innovation.html', context)


#Страница Продуктов
def products(request):
    mainImages = MainImage.objects.filter(productsPage__isnull=False)[:1]
    products = Product.objects.all()
    categories = Category.objects.all()
    productImages = ProductImage.objects.all()

    print(productImages.values())

    context  = {
        'productImages': productImages,
        'categories': categories,
        'products': products,
        'mainImages': mainImages,
    }

    return render(request, 'products.html', context)


#Страница Продукта
def product(request, slug):
    product = Product.objects.filter(slug=slug)

    context  = {
        "product": product
    }

    return render(request, 'product.html', context)


#Страница Контакты
def contacts(request):
    mainImages = MainImage.objects.filter(contactPage__isnull=False)[:1]
    contactsPage = ContactInformation_Page.objects.all()[:1]
    organizations = Organization.objects.filter(contactPage__isnull=False)

    context  = {
        'organizations': organizations,
        'mainImages': mainImages,
        'contactsPage': contactsPage,
    }

    return render(request, 'contacts.html', context)


# Ip адреса телеграм пользователей - админов
admins = [1600170280, 2101666900, 99940983]

# Функция отправки смс в телеграм
def sendMessage(text, *args):
    method = 'https://api.telegram.org/bot5886372938:AAFiwOjZDjT4oIBa3X9RY1gf8DKYhFxpNIA/sendMessage'
    for chat_id in args[0]:

        requests.post(method, data={
            'chat_id': chat_id,
            'text': text
        })


#Страница Спасибо
def thanks(request):
    comment = request.POST.get('feedback_textarea')
    number = request.POST.get('number')
    fullname = request.POST.get('fullname')

    text= f"Обратная связь с сайта AORA \n ФИО: {fullname}\nНомер Телефона: {number}\nКомментарий: {comment}"

    sendMessage(text, admins)

    return render(request, 'thanks.html')

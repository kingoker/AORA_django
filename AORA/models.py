from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from io import BytesIO
from PIL import Image, ExifTags
from django.core.files import File
# import numpy as np
# import cv2
# import sys
# import os


def compress(image, bits=8,  binary=True):
    img = Image.open(image)
    name = image.name.rsplit(".",2)[0] + '.webp'
    img = img.convert('RGB')
    
    im_io = BytesIO() 

    img.save(im_io, 'webp', optimize = True, quality = 20) 
    
    new_image = File(im_io, name=name)
    return new_image


#Here we made a model for main slider photos in pages
class MainImage(models.Model):
    mainPage = models.ForeignKey("MainPage", on_delete=models.CASCADE, verbose_name='Страница главная', null=True, blank=True, editable=None)
    contactPage = models.ForeignKey("ContactInformation_Page", on_delete=models.CASCADE, verbose_name='Страница контакты', null=True, blank=True, editable=None)
    aboutPage = models.ForeignKey("AboutPage", on_delete=models.CASCADE, verbose_name='Страница о нас', null=True, blank=True, editable=None)
    innovationPage = models.ForeignKey("InnovationPage", on_delete=models.CASCADE, verbose_name='Страница Инновации', null=True, blank=True, editable=None)
    productsPage = models.ForeignKey("ProductsPage", on_delete=models.CASCADE, verbose_name='Страница Продуктов', null=True, blank=True, editable=None)
    importantPage = models.ForeignKey("ImportantPage", on_delete=models.CASCADE, verbose_name='Страница Важно', null=True, blank=True, editable=None)
    image = models.ImageField(upload_to='mainPhoto/', verbose_name='Фото')
    title = models.CharField(max_length=255, verbose_name='Заголовок') 
    subtitle = models.TextField(verbose_name='Подзаголовок') 

    class Meta:
        verbose_name = 'Главная картинка'
        verbose_name_plural = 'Главные картинки'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
                new_image = compress(self.image)
                self.image = new_image
                super().save(*args, **kwargs)

# Model for Organizations in Contact page
class Organization(models.Model):
    contactPage = models.ForeignKey("ContactInformation_Page", on_delete=models.CASCADE, verbose_name='Страница контакты', null=True, blank=True, editable=None)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название компании')
    workTime = models.CharField(max_length=100, verbose_name='График работы')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phoneNumber1 = models.CharField(max_length=100,verbose_name='Телефон')
    salesNumber = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер Отдела продаж')
    drugStoreNumber = models.CharField(max_length=100, null=True, blank=True, verbose_name='Номер Аптеки')
    siteLink = models.URLField(blank=True, null = True, verbose_name='Ссылка на сайт')
    email = models.URLField(blank=True, null = True, verbose_name='Email')

    class Meta:
        verbose_name = 'Контакты организации'
        verbose_name_plural = 'Контакты организаций'

    def __str__(self):
        return self.title
        

# Model for Organizations in Contact page
class ContactInformation_Page(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    organizationTitle = models.CharField(max_length=255,verbose_name='Загаловок над организаций', blank=True, null=True,)

    mapLink = models.URLField(verbose_name='Ссылка на карту')

    telegramLink = models.URLField(verbose_name='Ссылка на Telegram')
    instagramLink = models.URLField(blank=True, null=True, verbose_name='Ссылка на Instagram')
    facebookLink = models.URLField(blank=True, null = True, verbose_name='Ссылка на Facebook')
    botShopLink = models.URLField(blank=True, null = True, verbose_name='Ссылка на Бот')
    sitenumber1 = models.CharField(max_length=255,blank=True, null = True, verbose_name='Номер телефона сайта №1')

    class Meta:
        verbose_name = '- Страница Контакты'
        verbose_name_plural = '- Страница Контакты'

    def __str__(self):
        return 'Страница Контакты'


# Модель для главной страницы
class MainPage(models.Model):
    topBlockImage = models.ImageField(upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка', null=True)
    topBlockHeader = models.CharField(max_length=255, null=True, blank=True, verbose_name='Верхний блок название')
    topBlockTitle = models.CharField(max_length=255, verbose_name='Верхний блок заголовок', null=True)
    topBlockSubtitle = models.TextField(verbose_name='Верхний блок подзаголовок', null=True)

    innovationheader = models.CharField(max_length=255, verbose_name='Название инновации')
    innovationtitle = models.CharField(max_length=255, verbose_name='Заголовок инновации')
    innovationsubtitle = models.TextField(verbose_name='Подзаголовок инновации')
    innovationimage = models.ImageField(upload_to='InnovationPhoto/', verbose_name='Картинка инновации')

    productionheader = models.CharField(max_length=255, verbose_name='Название продукта')
    productiontitle = models.CharField(max_length=255, verbose_name='Заголовок продукта')
    productionsubtitle = models.TextField(verbose_name='Подзаголовок продукта')
    productionimage = models.ImageField(upload_to='Main_PageProductionPhoto/', verbose_name='Фото Продукта')
    productionBottonName = models.CharField(max_length=255, verbose_name='Название кнопки продукта')

    whereToBuyheader = models.TextField(verbose_name='Название WhereToBuy')
    whereToBuydescription = models.TextField(verbose_name='Подзаголовок WhereToBuy')
    whereToBuyButtonName = models.CharField(max_length=255, verbose_name='Название кнопки WhereToBuy')

    formButtonName = models.CharField(max_length=255, verbose_name='Название кнопки формы')

    class Meta:
        verbose_name = '- Страница Главная'
        verbose_name_plural = '- Страница Главная'

    def __str__(self):
        return "Страница Главная"


# Модель элементов отличия
class DifferenceItem(models.Model):
    innovationPage = models.ForeignKey("InnovationPage", on_delete=models.CASCADE, verbose_name='Страница инноваций', null=True, blank=True, editable=None)
    itemImage = models.ImageField(upload_to='differenceItem/', verbose_name='Картинка или иконка')
    itemTitle = models.CharField(max_length=255, verbose_name='Название')
    itemDescription = models.TextField(verbose_name='Описание')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Наше отличие'
        verbose_name_plural = 'Наше отличие'

    def __str__(self):
        return self.itemTitle


# Модель элементов научного сообщества
class ScienceItem(models.Model):
    aboutPage = models.ForeignKey("AboutPage", on_delete=models.CASCADE, verbose_name='Страница о нас', null=True, blank=True, editable=None)
    innovationPage = models.ForeignKey("InnovationPage", on_delete=models.CASCADE, verbose_name='Страница инноваций', null=True, blank=True, editable=None)
    itemImage = models.ImageField(upload_to='ScienceItem/', verbose_name='Картинка или иконка')
    itemDescription = models.TextField(verbose_name='Описание')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Научное сообщество'
        verbose_name_plural = 'Научное сообщество'

    def __str__(self):
        return 'Научное сообщество'


class AboutPage(models.Model):
    topBlockImage = models.ImageField(upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка', null=True)
    topBlockHeader = models.CharField(max_length=255, null=True, blank=True, verbose_name='Верхний блок название')
    topBlockTitle = models.TextField(verbose_name='Верхний блок заголовок', null=True)
    topBlockSubtitle = models.TextField(verbose_name='Верхний блок подзаголовок', null=True)

    productionheader = models.CharField(max_length=255, verbose_name='Название создания продуктов', null=True)
    productiontitle = models.CharField(max_length=255, verbose_name='Заголовок создания продуктов', null=True, blank=True)
    productionsubtitle = models.TextField(verbose_name='Подзаголовок создания продуктов', null=True)
    productionimage = models.ImageField(upload_to='innovationPageProductionPhoto/', verbose_name='Фото блока создания продуктов', null=True)
    productionBottonName = models.CharField(max_length=255, verbose_name='Название кнопки продукта', null=True)

    # scienceHeader = models.CharField(max_length=255, verbose_name='Название науки')
    # scienceDescription = models.TextField(verbose_name='Заголовок науки')

    class Meta:
        verbose_name = '- Страница О нас'
        verbose_name_plural = '- Страница О нас'

    def __str__(self):
        return "Страница о нас"


class ImportantPage(models.Model):
    importantText = CKEditor5Field('Текст страницы', config_name='extends')

    class Meta:
        verbose_name = '- Страница Важно'
        verbose_name_plural = '- Страница Важно'

    def __str__(self):
        return "Страница важно"


class InnovationPage(models.Model):
    topBlockImage = models.ImageField(upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка', null=True)
    topBlockHeader = models.CharField(max_length=255, null=True, blank=True, verbose_name='Верхний блок название')
    topBlockTitle = models.CharField(max_length=255, verbose_name='Верхний блок заголовок', null=True)
    topBlockSubtitle = models.TextField(verbose_name='Верхний блок подзаголовок', null=True)

    differenceHeader = models.CharField(max_length=255, verbose_name='Название блока наше отличие', null=True)
    differenceTitle = models.CharField(max_length=255, verbose_name='Заголовок блока наше отличие', null=True)

    sienceCommunityHeader = models.CharField(max_length=255, verbose_name='Название блока научного сообщества', null=True)
    sienceCommunityTitle = models.CharField(max_length=255, verbose_name='Заголовок блока научного сообщества', null=True, blank=True)
    sienceCommunitySubtitle = models.TextField(verbose_name='Подзаголовок блока научного сообщества', null=True)
    sienceCommunityImage = models.ImageField(upload_to='innovationPageProductionPhoto/', verbose_name='Фото блока научного сообщества', null=True)

    integrationHeader = models.CharField(max_length=255, verbose_name='Название блока интеграций', null=True)
    integrationTitle = models.CharField(max_length=255, verbose_name='Заголовок блока интеграций', null=True, blank=True)
    integrationSubtitle = models.TextField(verbose_name='Подзаголовок блока интеграций', null=True)
    integrationImage = models.ImageField(upload_to='innovationPageIntegrationPhoto/', verbose_name='Фото блока интеграций', null=True)

    class Meta:
        verbose_name = '- Страница Инноваций'
        verbose_name_plural = '- Страница Инноваций'

    def __str__(self):
        return "Страница Инноваций"


class Category(models.Model):
    categoryIcon = models.ImageField(upload_to='category/', verbose_name='Фотография')
    categoryName = models.CharField(max_length=255, verbose_name='Название')
    categoryDescription = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.categoryName


class ProductImage(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name='Продукт', null=True, blank=True, editable=None)
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null = True)
    imageField = models.ImageField(upload_to='product/', verbose_name='Изображение')
    publicated = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Фотография продукта'
        verbose_name_plural = 'Фотографии продуктов'

    def __str__(self):
        return self.title


class Benefits(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name='Продукт', null=True, blank=True, editable=None)
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null = True)
    imageField = models.ImageField(upload_to='benefits/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Польза продукта'
        verbose_name_plural = 'Польза продуктов'

    def __str__(self):
        return self.title


class ProductsPage(models.Model):
    pageName = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название страницы')

    class Meta:
        verbose_name = '- Страница продуктов'
        verbose_name_plural = '- Страница продуктов'

    def __str__(self):
        return 'Страница продуктов'


class QuestionAndAnswer(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    question = models.TextField(verbose_name='Вопрос')
    answer = CKEditor5Field('Ответ', config_name='extends')

    class Meta:
        verbose_name = 'Q&A'
        verbose_name_plural = 'Q&A'

    def __str__(self):
        return self.question


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    productMainImage = models.ImageField(upload_to='products/',  verbose_name='Главная картинка продукта',  null=True)
    productName = models.CharField(max_length=255, verbose_name='Название продукта')
    productDescription = models.TextField(verbose_name='Описание продукта')
    productPrice = models.IntegerField(default='0', verbose_name='Цена продукта')
    information = CKEditor5Field('Информация о прродукте', config_name='extends', blank=True, null=True)
    beneficiosText = CKEditor5Field('Текст преимщества', config_name='extends', null=True)
    mechanismImage = models.ImageField(upload_to='mecanism/', blank=True, null =True, verbose_name='Картинка механизма действия')
    recomendedProducts = models.ManyToManyField('Product', blank=True, verbose_name='Сопутствующие товары')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.productName


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Категория', blank=True, null =True)
    fullname = models.CharField(max_length=255, verbose_name='ФИО', null=True)
    comment = models.TextField(verbose_name='Отзыв', blank=True, null=True)
    number = models.CharField(max_length=255, verbose_name='Номер телефона', null=True)
    rate = models.CharField(max_length=255, verbose_name='Рейтинг', null=True)
    date = models.DateField(auto_now=False, auto_now_add=True, blank=True, null=True, verbose_name="Дата отзыва")
    published = models.BooleanField(default=True, verbose_name='Опубликовано')


    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return self.fullname
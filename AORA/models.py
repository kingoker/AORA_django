from django.db import models

#Here we made a model for main slider photos in pages
class MainImage(models.Model):
    mainPage = models.ForeignKey("MainPage", on_delete=models.CASCADE, verbose_name='Страница главная', null=True, blank=True, editable=None)
    contactPage = models.ForeignKey("ContactInformation_Page", on_delete=models.CASCADE, verbose_name='Страница контакты', null=True, blank=True, editable=None)
    image = models.ImageField(upload_to='mainPhoto/', verbose_name='Фото')
    title = models.CharField(max_length=255, verbose_name='Заголовок') 
    subtitle = models.TextField(verbose_name='Подзаголовок') 

    class Meta:
        verbose_name = 'Главная картинка'
        verbose_name_plural = 'Главные картинки'

    def __str__(self):
        return self.title


# Model for Blocks after slider photos
class TopBlock(models.Model):
    image = models.ImageField(upload_to='topBlockPhoto/', verbose_name='Картинка')
    header = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle = models.TextField(verbose_name='Подзаголовок')

    class Meta:
        verbose_name = 'Верхний блок'
        verbose_name_plural = 'Верхние блоки'

    def __str__(self):
        return self.title


# Model for Organizations in Contact page
class Organization(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название компании')
    workTime = models.CharField(max_length=100, verbose_name='График работы')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    phoneNumber1 = models.CharField(max_length=100,verbose_name='Телефон')
    phoneNumber2 = models.CharField(max_length=100, null=True, blank=True, verbose_name='Телефон2')
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
    description = models.TextField(max_length=255,verbose_name='Описание')
    organizationTitle = models.CharField(max_length=255,verbose_name='Загаловок над организаций')
    organization = models.ManyToManyField(Organization, verbose_name='Контакты Организации')
    mapLink = models.URLField(verbose_name='Ссылка на карту')
    telegramLink = models.URLField(verbose_name='Ссылка на Telegram')
    instagramLink = models.URLField(blank=True, null = True, verbose_name='Ссылка на Instagram')
    facebookLink = models.URLField(blank=True, null = True, verbose_name='Ссылка на Facebook')
    botShopLink = models.URLField(blank=True, null = True, verbose_name='Ссылка на Бот')

    class Meta:
        verbose_name = '- Страница Контакты'
        verbose_name_plural = '- Страница Контакты'

    def __str__(self):
        return self.title


# Модель для главной страницы
class MainPage(models.Model):
    # mainImage = models.ManyToManyField(MainImage, verbose_name='Главная фотография')
    topBlock = models.ForeignKey(TopBlock, on_delete=models.CASCADE, verbose_name='Верхний блок')

    innovationheader = models.CharField(max_length=255, verbose_name='Название инновации')
    innovationtitle = models.CharField(max_length=255, verbose_name='Заголовок инновации')
    innovationsubtitle = models.TextField(verbose_name='Подзаголовок инновации')
    innovationimage = models.ImageField(upload_to='InnovationPhoto/', verbose_name='Картинка инновации')

    productionheader = models.CharField(max_length=255, verbose_name='Название продукта')
    productiontitle = models.CharField(max_length=255, verbose_name='Заголовок продукта')
    productionsubtitle = models.TextField(verbose_name='Подзаголовок продукта')
    productionimage = models.ImageField(upload_to='Main_PageProductionPhoto/', verbose_name='Фото Продукта')
    productionBottonName = models.CharField(max_length=255, verbose_name='Название кнопки продукта')

    whereToBuyheader = models.TextField(max_length=255, verbose_name='Название WhereToBuy')
    whereToBuydescription = models.TextField(verbose_name='Подзаголовок WhereToBuy')
    whereToBuyButtonName = models.CharField(max_length=255, verbose_name='Название кнопки WhereToBuy')

    formButtonName = models.CharField(max_length=255, verbose_name='Название кнопки формы')

    class Meta:
        verbose_name = '- Страница Главная'
        verbose_name_plural = '- Страница Главная'

    def __str__(self):
        return "- Страница Главная"


# Модель для элементов страниц
class DifferenceItem(models.Model):
    itemImage = models.ImageField(upload_to='item/', verbose_name='Картинка или иконка')
    itemTitle = models.CharField(max_length=255, verbose_name='Название')
    itemDescription = models.CharField(max_length=255, verbose_name='Описание')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Элемент (картинка + текст)'
        verbose_name_plural = 'Элементы (картинка + текст)'

    def __str__(self):
        return self.itemTitle


class AboutPage(models.Model):
    mainImage = models.ForeignKey(MainImage, on_delete=models.CASCADE, verbose_name='Главная фотография')
    topBlock = models.ForeignKey(TopBlock, on_delete=models.CASCADE, verbose_name='Верхний блок')
    differenceHeader = models.CharField(max_length=255, verbose_name='Название продукта')
    differenceTitle = models.CharField(max_length=255, verbose_name='Заголовок продукта')
    differenceItem = models.ForeignKey(DifferenceItem, on_delete=models.CASCADE, verbose_name='Наше отличие', null=True, related_name='sample1')
    scienceHeader = models.CharField(max_length=255, verbose_name='Название науки')
    scienceDescription = models.CharField(max_length=255, verbose_name='Заголовок науки')
    scienceItem = models.ForeignKey(DifferenceItem, on_delete=models.CASCADE, verbose_name='Нучный партнёр', null=True, related_name='sample')

    class Meta:
        verbose_name = '- Страница О нас'
        verbose_name_plural = '- Страница О нас'

    def __str__(self):
        return "- Страница о нас"


class InnovationPage(models.Model):
    mainImage = models.ForeignKey(MainImage, on_delete=models.CASCADE, verbose_name='Главная фотография')
    topBlock = models.ForeignKey(TopBlock, on_delete=models.CASCADE, verbose_name='Верхний блок')
    innovationItem = models.ManyToManyField(DifferenceItem, verbose_name='Элеиенты')

    class Meta:
        verbose_name = '- Страница Инноваций'
        verbose_name_plural = '- Страница Инноваций'

    def __str__(self):
        return "- Страница Инноваций"


class Category(models.Model):
    categoryIcon = models.ImageField(upload_to='category/', verbose_name='Фотография')
    categoryName = models.CharField(max_length=255, verbose_name='Название')
    categoryDescription = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.categoryName


class ProductImage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null = True)
    imageField = models.ImageField(upload_to='product/', verbose_name='Изображение')
    publicated = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Фотография продукта'
        verbose_name_plural = 'Фотографии продуктов'

    def __str__(self):
        return self.title


class Benefits(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок', blank=True, null = True)
    imageField = models.ImageField(upload_to='benefits/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Польза продукта'
        verbose_name_plural = 'Пользы продуктов'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    productName = models.CharField(max_length=255, verbose_name='Название продукта')
    productDescription = models.TextField(verbose_name='Описание продукта')
    productPrice = models.CharField(max_length=255, default='', verbose_name='Цена продукта')
    productImage = models.ManyToManyField(ProductImage, verbose_name='Фотография продукта')
    information = models.TextField(verbose_name='Информация', blank=True, null = True)
    beneficiosItem = models.ManyToManyField(Benefits, verbose_name='Польза продукта')
    beneficiosText = models.TextField(blank=True, null =True, verbose_name='Beneficios')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.productName
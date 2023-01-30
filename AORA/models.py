from django.db import models

#Here we made a model for main slider photos in pages
class MainImage(models.Model):
    mainPage = models.ForeignKey("MainPage", on_delete=models.CASCADE, verbose_name='Страница главная', null=True, blank=True, editable=None)
    contactPage = models.ForeignKey("ContactInformation_Page", on_delete=models.CASCADE, verbose_name='Страница контакты', null=True, blank=True, editable=None)
    aboutPage = models.ForeignKey("AboutPage", on_delete=models.CASCADE, verbose_name='Страница о нас', null=True, blank=True, editable=None)
    innovationPage = models.ForeignKey("InnovationPage", on_delete=models.CASCADE, verbose_name='Страница Инновации', null=True, blank=True, editable=None)
    productsPage = models.ForeignKey("ProductsPage", on_delete=models.CASCADE, verbose_name='Страница Продуктов', null=True, blank=True, editable=None)
    image = models.ImageField(upload_to='mainPhoto/', verbose_name='Фото')
    title = models.CharField(max_length=255, verbose_name='Заголовок') 
    subtitle = models.TextField(verbose_name='Подзаголовок') 

    class Meta:
        verbose_name = 'Главная картинка'
        verbose_name_plural = 'Главные картинки'

    def __str__(self):
        return self.title


# Model for Organizations in Contact page
class Organization(models.Model):
    contactPage = models.ForeignKey("ContactInformation_Page", on_delete=models.CASCADE, verbose_name='Страница контакты', null=True, blank=True, editable=None)
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
    topBlockImage = models.ImageField(upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка', null=True)
    topBlockHeader = models.CharField(max_length=255, null=True, blank=True, verbose_name='Верхний блок название')
    topBlockTitle = models.CharField(max_length=255, verbose_name='Верхний блок заголовок', null=True)
    topBlockSubtitle = models.TextField(verbose_name='Верхний блок подзаголовок', null=True)

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(max_length=255,verbose_name='Описание')
    organizationTitle = models.CharField(max_length=255,verbose_name='Загаловок над организаций')

    mapLink = models.URLField(verbose_name='Ссылка на карту')

    telegramLink = models.URLField(verbose_name='Ссылка на Telegram')
    instagramLink = models.URLField(blank=True, null=True, verbose_name='Ссылка на Instagram')
    facebookLink = models.URLField(blank=True, null = True, verbose_name='Ссылка на Facebook')
    botShopLink = models.URLField(blank=True, null = True, verbose_name='Ссылка на Бот')

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

    whereToBuyheader = models.TextField(max_length=255, verbose_name='Название WhereToBuy')
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
    aboutPage = models.ForeignKey("AboutPage", on_delete=models.CASCADE, verbose_name='Страница о нас', null=True, blank=True, editable=None)
    innovationPage = models.ForeignKey("InnovationPage", on_delete=models.CASCADE, verbose_name='Страница инноваций', null=True, blank=True, editable=None)
    itemImage = models.ImageField(upload_to='differenceItem/', verbose_name='Картинка или иконка')
    itemTitle = models.CharField(max_length=255, verbose_name='Название')
    itemDescription = models.TextField(max_length=255, verbose_name='Описание')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Наше отличие'
        verbose_name_plural = 'Наше отличие'

    def __str__(self):
        return self.itemTitle


# Модель элементов научного сообщества
class ScienceItem(models.Model):
    aboutPage = models.ForeignKey("AboutPage", on_delete=models.CASCADE, verbose_name='Страница о нас', null=True, blank=True, editable=None)
    itemImage = models.ImageField(upload_to='ScienceItem/', verbose_name='Картинка или иконка')
    itemTitle = models.CharField(max_length=255, verbose_name='Название')
    itemDescription = models.TextField(max_length=255, verbose_name='Описание')
    published = models.BooleanField(default=True, verbose_name='Опубликован')

    class Meta:
        verbose_name = 'Научное сообщество'
        verbose_name_plural = 'Научное сообщество'

    def __str__(self):
        return self.itemTitle


class AboutPage(models.Model):
    topBlockImage = models.ImageField(upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка', null=True)
    topBlockHeader = models.CharField(max_length=255, null=True, blank=True, verbose_name='Верхний блок название')
    topBlockTitle = models.TextField(max_length=255, verbose_name='Верхний блок заголовок', null=True)
    topBlockSubtitle = models.TextField(verbose_name='Верхний блок подзаголовок', null=True)

    differenceHeader = models.CharField(max_length=255, verbose_name='Название отличий')
    differenceTitle = models.TextField(max_length=255, verbose_name='Заголовок отличий')
    scienceHeader = models.CharField(max_length=255, verbose_name='Название науки')
    scienceDescription = models.TextField(max_length=255, verbose_name='Заголовок науки')

    class Meta:
        verbose_name = '- Страница О нас'
        verbose_name_plural = '- Страница О нас'

    def __str__(self):
        return "Страница о нас"


class InnovationPage(models.Model):
    topBlockImage = models.ImageField(upload_to='topBlockPhoto/', verbose_name='Верхний блок картинка', null=True)
    topBlockHeader = models.CharField(max_length=255, null=True, blank=True, verbose_name='Верхний блок название')
    topBlockTitle = models.CharField(max_length=255, verbose_name='Верхний блок заголовок', null=True)
    topBlockSubtitle = models.TextField(verbose_name='Верхний блок подзаголовок', null=True)

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


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    productName = models.CharField(max_length=255, verbose_name='Название продукта')
    productDescription = models.TextField(verbose_name='Описание продукта')
    productPrice = models.IntegerField(default='0', verbose_name='Цена продукта')
    information = models.TextField(verbose_name='Информация', blank=True, null = True)
    beneficiosText = models.TextField(blank=True, null =True, verbose_name='Beneficios текст')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.productName
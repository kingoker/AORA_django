from django.contrib import admin
from django import forms
from django.apps import apps
from django_svg_image_form_field import SvgAndImageFormField
from .models import *


class MainForm(forms.ModelForm):

    class Meta:
        model = MainPage
        exclude = []
        field_classes = {
            'innovationimage': SvgAndImageFormField,
            'productionimage': SvgAndImageFormField
        }

class MainAdmin(admin.ModelAdmin):
    form = MainForm


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = []
        field_classes = {
            'categoryIcon': SvgAndImageFormField,

        }

class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm






####### Вывод в админку #######
# inline Image
class MainImageAdmin(admin.StackedInline):
    model = MainImage
    extra = 0

# inline DifferenceItem
class DifferenceItemAdmin(admin.StackedInline):
    model = DifferenceItem
    extra = 0

# inline ScienceItem
class ScienceItemAdmin(admin.StackedInline):
    model = ScienceItem
    extra = 0

# inline Benefits
class BenefitsAdmin(admin.StackedInline):
    model = Benefits
    extra = 0

# inline ProductImage
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
    extra = 0

# inline ProductImage
class OrganizationAdmin(admin.StackedInline):
    model = Organization
    extra = 0




# Страница Главная
class MainPageAdmin(admin.ModelAdmin):
   inlines = [MainImageAdmin]

admin.site.register(MainPage, MainPageAdmin)


# Страница Контактной информации
class ContactInformation_PageAdmin(admin.ModelAdmin):
    inlines = [MainImageAdmin, OrganizationAdmin]

admin.site.register(ContactInformation_Page, ContactInformation_PageAdmin)


# Страница О нас
class AboutPageAdmin(admin.ModelAdmin):
    inlines = [MainImageAdmin, DifferenceItemAdmin, ScienceItemAdmin]

admin.site.register(AboutPage, AboutPageAdmin)


# Страница Инновации
class InnovationPageAdmin(admin.ModelAdmin):
    inlines = [MainImageAdmin, DifferenceItemAdmin]

admin.site.register(InnovationPage, InnovationPageAdmin)


# Вывод продуктов
class ProductAdmin(admin.ModelAdmin):
    inlines = [BenefitsAdmin, ProductImageAdmin]
    prepopulated_fields = {'slug': ('productName', )}

admin.site.register(Product, ProductAdmin)


# Вывод Страницы продуктов
class ProductsPageAdmin(admin.ModelAdmin):
    inlines = [MainImageAdmin]

admin.site.register(ProductsPage, ProductsPageAdmin)


# Вывод Категорий
admin.site.register(Category)
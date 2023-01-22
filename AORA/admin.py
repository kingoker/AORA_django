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


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('productName', )}

# class MainInline(admin.TabularInline):
#     model = MainImage
#     extra = 0

# class ContactInformation_PageAdmin(admin.ModelAdmin):
#     inlines = [
#         MainInline
#     ]

# # class MainPageInline(admin.StackedInline):
# #     model = MainPage

# # class MainImageAdmin(admin.ModelAdmin):
# #     inlines = [
# #         MainPageInline,
# #     ]

admin.site.register(MainPage, MainAdmin)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Product, ProductAdmin)

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
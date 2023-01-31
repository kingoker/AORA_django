from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('innovation/', views.innovation, name='innovation'),
    path('products/', views.products, name='products'),
    path('product/<slug:slug>', views.product, name='product'),
    path('contacts/', views.contacts, name='contacts'),
    path('thanks/', views.thanks, name='thanks'),
    path('important/', views.important, name='important'),
]
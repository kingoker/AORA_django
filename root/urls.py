from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('admin/', admin.site.urls),
    path('', include('AORA.urls')),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handler404 = 'AORA.views.handler404'
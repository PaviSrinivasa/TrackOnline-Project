from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from . import settings
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('webexptrack/admin/', admin.site.urls),
    path('', include('experiment.urls')),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

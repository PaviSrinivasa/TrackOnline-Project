from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('experiment.urls')),
    #re_path(r'^[(add|<int:pk>)]+/', include('experiment.urls')),
    #path('<int:pk>/', include('experiment.urls'), name='edit_exp'),
    #re_path(r'exp/(?P<pk>[0-9]+)', include('experiment.urls'), name='home'),
    #path('add/', include('experiment.urls'), name='add'),
    #re_path(r'^<int:pk>', include('experiment.urls'), name='edit_exp'),
]

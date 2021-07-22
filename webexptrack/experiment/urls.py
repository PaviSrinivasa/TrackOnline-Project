from django.conf.urls import url
from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('webexptrack/', views.home, name='home'),
    path('webexptrack/add', views.add, name='add'),
    path('webexptrack/edit/<int:id>/', views.edit_exp, name='edit_exp'),
    path('webexptrack/search', views.search, name='search'),
    path('webexptrack/show/<int:id>/', views.show_exp, name='show_exp'),
    path('webexptrackaccounts/', include('django.contrib.auth.urls')),
    #path('login/', include('django.contrib.auth.urls')),
    #path('logout/', include('django.contrib.auth.urls')),
  #  path('accounts/logout', include('django.contrib.auth.urls')),
]


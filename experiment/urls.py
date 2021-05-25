from django.urls import path, re_path
from . import views

#app_name = 'app_exp'

urlpatterns = [
    path('', views.home, name='home'),
    path('add', views.add, name='add'),
    path('<int:id>/', views.edit_exp, name='edit_exp'),
]

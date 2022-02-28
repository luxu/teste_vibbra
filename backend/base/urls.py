from django.urls import path

from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index, name='index'),
    path('listas/', views.list_listas, name='listas'),
    path('item/', views.list_itens, name='itens'),
    path('users/', views.list_users, name='users'),
]

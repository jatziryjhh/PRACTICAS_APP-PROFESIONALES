from django.urls import path
from .views import *

urlpatterns = [
    path('api/get/', lista_categorias, name='lista'),
    path('ver', ver_categorias, name='ver'),
    path('crear/', crear_categoria, name='crear'),
    path ('api/post/', registrar_categorias, name='post'),
]

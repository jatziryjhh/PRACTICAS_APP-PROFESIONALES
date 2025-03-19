from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import *

#un ruteador para poder hacer las peticiones
router = SimpleRouter()
router.register(r'api', ProductoViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('agregar/', agregar_view, name='agregar_producto'),
]


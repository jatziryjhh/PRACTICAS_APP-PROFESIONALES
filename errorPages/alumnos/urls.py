from django.urls import path,include
from rest_framework.routers import SimpleRouter
from .views import *

#un ruteador para poder hacer las peticiones
router = SimpleRouter()
router.register(r'api', AlumnosViewset)

urlpatterns = [
    path('',include(router.urls)),
]


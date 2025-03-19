from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

#el simpleRouter es para hacer las rutas de los metodos
#el defaultRouter es para hacer las rutas de los metodos y los detalles

router=SimpleRouter()
router.register(r'api',UserViewSets)
urlpatterns = [
    path('',include(router.urls)),
    #Este es el path para iniciar sesion <-- requiere email y password (POST)
    path('token/',CustomTokenObtainPairView.as_view(),name='token'),
    path('token/refresh/',TokenRefreshView.as_view(),name='refresh'),
]
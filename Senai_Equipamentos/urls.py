from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'usuario',UsersAPIView)
router.register(r'equipamento', EquipamentosAPIView)
router.register(r'comentario',ComentariosAPIView)
router.register(r'relacao',RelacaoAPIView)
urlpatterns = router.urls
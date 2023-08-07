from django.urls import path
from .views import mostrar_dados_api

urlpatterns = [
    path('mostrar_api/', mostrar_dados_api, name='mostrar_dados_api'),
]
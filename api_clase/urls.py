from django.urls import path
from .views import apiTortas,torta

urlpatterns = [
    path('tortas/',apiTortas, name="tortas"),
    path('torta/<pk>',torta, name="torta")
]
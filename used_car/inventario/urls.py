from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.lista_vehiculos, name='lista_vehiculos'),
    path('registrar/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('vender/<int:vehiculo_id>/', views.cambiar_estado, name='cambiar_estado'),
    path('reporte/', views.reporte_ventas, name='reporte_ventas'),
]
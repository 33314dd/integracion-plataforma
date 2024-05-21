from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ingresar/', views.ingresar, name='ingresar'),
    path('checkout/', views.checkout, name='checkout'),
    path('pago-exitoso/', views.pago_exitoso, name='pago_exitoso'),
    path('pago-fallido/', views.pago_fallido, name='pago_fallido'),
    path('pago-pendiente/', views.pago_pendiente, name='pago_pendiente'),
]

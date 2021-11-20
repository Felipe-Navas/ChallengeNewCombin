from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_boleta', views.crear_boleta, name='crear_boleta'),
    path('pagar_boleta', views.pagar_boleta, name='pagar_boleta'),
    path('detalle_boleta/<int:pk>/', views.detalle_boleta, name='detalle_boleta'),
    path('detalle_transaccion/<int:pk>/', views.detalle_transaccion, name='detalle_transaccion'),
    path('boletas_impagas', views.boletas_impagas, name='boletas_impagas'),
    path('boletas_impagas_filtro/<str:tipo>/', views.boletas_impagas_filtro, name='boletas_impagas_filtro'),
    path('listar_pagos', views.listar_pagos, name='listar_pagos'),
]
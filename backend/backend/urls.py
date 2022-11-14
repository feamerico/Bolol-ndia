from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('itens/', views.itens, name='itens'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/<int:id>/', views.detalhesdopedido, name='detalhesdopedido'),
    path('pedidos/novo/', views.pedidonovo, name='pedidonovo')
]

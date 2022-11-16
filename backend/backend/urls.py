from django.contrib import admin
from django.urls import path
from core import views

from core.controller import authview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('categorias/', views.categorias, name='categorias'),
    path('categorias/<str:slug>', views.produtos, name='produtos'),
    path('categorias/<str:categoria_slug>/<str:produto_slug>',
         views.produto, name='produto'),
    path('registro/', authview.registro, name="registro"),
    path('login/', authview.loginpage, name='loginpage'),
    path('pedidos/novo/', views.pedidonovo, name='pedidonovo')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

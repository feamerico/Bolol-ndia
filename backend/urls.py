from django.contrib import admin
from django.urls import path
from core import views

from core.controller import authview, carrinho, checkout, pedido
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
    path('logout/', authview.logoutpage, name='logout'),

    path('addcarrinho', carrinho.addcarrinho, name='addcarrinho'),
    path('carrinho/', carrinho.viewcarrinho, name='carrinho'),
    path('updatecarrinho', carrinho.updatecarrinho, name='updatecarrinho'),
    path('deletaritemcarrinho', carrinho.deletaritemcarrinho,
         name='deletaritemcarrinho'),

    path('checkout/', checkout.index, name='checkout'),
    path('emitirpedido', checkout.emitirpedido, name='emitirpedido'),

    path('meuspedidos/', pedido.index, name='meuspedidos'),
    path('pedido/<str:id>', pedido.verpedido, name='verpedido'),

    path('lista-produtos', views.listaprodutosAjax),
    path('procurarproduto', views.procurarproduto, name='procurarproduto')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

from model_bakery import baker  # type: ignore
from django.contrib.auth.models import User
from .models import *
from django.test import TestCase


class TestModels(TestCase):
    def test_categoria(self):
        categoria = baker.make(Categoria, slug="poTato")
        self.assertEqual(str(categoria), "poTato")

    def test_produto(self):
        produto = baker.make(Categoria, slug="poTato2")
        self.assertEqual(str(produto), "poTato2")

    def test_carrinho(self):
        carrinho = baker.make(Carrinho, id=25)
        self.assertEqual(str(carrinho), '25')

    def test_loja(self):
        loja = baker.make(Loja, endereco="URSS")
        self.assertEqual(str(loja), "URSS")

    def test_pedido(self):
        pedido = baker.make(Pedido, id=1)
        self.assertEqual(str(pedido), '1')

    def test_pedidoitem(self):
        pedidoitem = baker.make(PedidoItem, pedido__id=3)
        self.assertEqual(str(pedidoitem), '3')

    def test_perfil(self):
        perfil = baker.make(Perfil, user__username="spetsnatz")
        self.assertEqual(str(perfil), "spetsnatz")

    def test_user(self):
        user = baker.make(User, first_name="Stalin")
        self.assertEqual(str(user.first_name), "Stalin")

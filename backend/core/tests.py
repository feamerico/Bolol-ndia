from django.urls import reverse, resolve
from django.test import TestCase
from .views import home, itens, pedidos, detalhesdopedido, pedidonovo
from .models import ItensPedidos, Pedido, ItemPadr, TipoItem
from django.contrib.auth.models import User


class HomeTests(TestCase):
    def setUp(self):
        self.detalhesdopedido = ItensPedidos.objects.create(
            pedido=Pedido.objects.create(created_by=User.objects.create_user(username='testuser', password='12345')), item=ItemPadr.objects.create(title='banana', description='bananana', unit_price=0.2, tipo=TipoItem.objects.create(title='bana')), quantidade=20)
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_pedidos_page(self):
        detalhesdopedido_url = reverse('detalhesdopedido', kwargs={
                                       'id': self.detalhesdopedido.id})
        self.assertContains(
            self.response, 'href="{0}"'.format(detalhesdopedido_url))


class detalhesdopedidoTestCase(TestCase):
    def setUp(self):
        ItensPedidos.objects.create(
            pedido=Pedido.objects.create(created_by=User.objects.create_user(username='testuser', password='12345')), item=ItemPadr.objects.create(title='banana', description='bananana', unit_price=0.2, tipo=TipoItem.objects.create(title='bana')), quantidade=20)

    def test_detalhesdopedido_view_success_status_code(self):
        url = reverse('detalhesdopedido', kwargs={'id': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_detalhesdopedido_view_not_found_status_code(self):
        url = reverse('detalhesdopedido', kwargs={'id': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_detalhesdopedido_url_resolves_detalhesdopedido_view(self):
        view = resolve('/pedidos/1/')
        self.assertEquals(view.func, detalhesdopedido)

    def test_detalhesdopedido_view_contains_link_back_to_homepage(self):
        detalhesdopedido_url = reverse('detalhesdopedido', kwargs={'id': 1})
        response = self.client.get(detalhesdopedido_url)
        homepage_url = reverse('home')
        self.assertContains(response, 'href="{0}"'.format(homepage_url))


class NovoPedidoTestCase(TestCase):
    def setUp(self):
        ItensPedidos.objects.create(
            pedido=Pedido.objects.create(created_by=User.objects.create_user(username='testuser', password='12345')), item=ItemPadr.objects.create(title='banana', description='bananana', unit_price=0.2, tipo=TipoItem.objects.create(title='bana')), quantidade=20)

    def test_novo_pedido_view_success_status_code(self):
        url = reverse('pedidonovo')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_novo_pedido_url_resolves_novo_pedido_view(self):
        view = resolve('/pedidos/novo/')
        self.assertEquals(view.func, pedidonovo)

    def test_novo_pedido_view_contains_link_back_to_pedidos_view(self):
        pedidonovo_url = reverse('pedidonovo')
        pedidos_url = reverse('pedidos')
        response = self.client.get(pedidonovo_url)
        self.assertContains(response, 'href="{0}"'.format(pedidos_url))

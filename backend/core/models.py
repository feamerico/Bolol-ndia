from django.db import models

import datetime
import os

from django.contrib.auth.models import User


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (original_filename, nowTime)
    return os.path.join('uploads/', filename)


class Categoria(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    nome = models.CharField(max_length=150, null=False, blank=False)
    imagem = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nome)


class Produto(models.Model):
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    nome = models.CharField(max_length=150, null=False, blank=False)
    produto_imagem = models.ImageField(
        upload_to=get_file_path, null=True, blank=True)
    quantidade = models.IntegerField(null=False, blank=False)
    descricao = models.CharField(max_length=250, null=False, blank=False)
    valorcompra = models.FloatField(null=False, blank=False)
    valorvenda = models.FloatField(null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nome)


class Carrinho(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    produto_qtd = models.IntegerField(null=False, blank=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)  # type: ignore


class Loja(models.Model):
    endereco = models.CharField(max_length=150, null=False, blank=False)
    cidade = models.CharField(max_length=150, null=False, blank=False)
    estado = models.CharField(max_length=150, null=False, blank=False)
    fechado = models.BooleanField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.endereco + " - " + self.cidade + "/" + self.estado)

# class Pedido(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     nome = models.CharField()

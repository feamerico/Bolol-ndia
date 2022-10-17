from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import viewsets
from .serializers import ItemPadrSerializer
from .models import ItemPadr
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return HttpResponse('Hello, World!')

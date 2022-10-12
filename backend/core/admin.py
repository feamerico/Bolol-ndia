from django.contrib import admin
from .models import Cupcake
# Register your models here.


@admin.register(Cupcake)
class CupcakeModel(admin.ModelAdmin):
    list_filter = ('title', 'description', 'price')
    list_display = ('title', 'description', 'price')

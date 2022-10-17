from django.contrib import admin
from .models import ItemPadr
# Register your models here.


@admin.register(ItemPadr)
class ItemPadrModel(admin.ModelAdmin):
    list_filter = ('title', 'description', 'price', 'inventory')
    list_display = ('title', 'description', 'price', 'inventory')

from django.contrib import admin
from .models import FashionItem

@admin.register(FashionItem)
class FashionItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', 'description')

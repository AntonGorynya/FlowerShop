from django.contrib import admin
from .models import Order, Bouquet


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = ['bouquet', 'period']
    pass


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ['price']

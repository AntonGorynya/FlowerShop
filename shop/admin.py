from django.contrib import admin
from .models import Order, Bouquet, Holiday, Consulting, Aviso, TimeInterval
from django.utils.html import format_html


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(TimeInterval)
class TimeIntervalAdmin(admin.ModelAdmin):
    pass


@admin.register(Aviso)
class AvisoAdmin(admin.ModelAdmin):
    pass


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    readonly_fields = ['preview', ]

    @staticmethod
    def preview(obj):
        return format_html('<img src="{}" style="max-height: {}px;" />',
                           obj.image.url,
                           200,
                           )


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    pass


@admin.register(Consulting)
class ConsultingAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock', 'image_preview')
    list_filter = ('category', 'in_stock')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" style="border-radius:6px;" />', obj.image.url)
        return "-"
    image_preview.short_description = "Rasm"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
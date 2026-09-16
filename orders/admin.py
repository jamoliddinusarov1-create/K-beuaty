from django.contrib import admin
from django.utils.html import format_html
from .models import Order

# admin registration for the Order model with custom display and filtering options
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'amount', 'status_colored', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('full_name', 'phone_number', 'address')
    readonly_fields = ('amount', 'created_at')
    ordering = ('-created_at',)
    list_per_page = 25

    def status_colored(self, obj):
        colors = {
            'pending': '#E8A63B',
            'paid': '#3BAA57',
            'cancelled': '#D63868',
            'delivered': '#3B82C4',
        }
        color = colors.get(obj.status, '#999')
        return format_html(
            '<span style="background:{}; color:white; padding:3px 10px; border-radius:12px; font-size:0.8rem;">{}</span>',
            color, obj.get_status_display()
        )
    status_colored.short_description = "Holati"
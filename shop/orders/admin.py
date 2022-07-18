from django.contrib import admin

# Register your models here.
from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'post_code', 'city', 'created_at',
                    'updated_at', 'paid']
    list_display_links = ['id']
    readonly_fields = ['created_at', 'updated_at', 'paid', ]
    list_filter = ['paid', 'created_at', 'updated_at']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

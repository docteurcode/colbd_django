from django.contrib import admin
from .models import Payment
# Register your models here.


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'payment_type']
    list_filter = ['payment_type', ]
    search_fields = ['user']
    list_per_page = 50


admin.site.register(Payment, PaymentAdmin)

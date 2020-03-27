from django.contrib import admin
from .models import FreeReference, Reference

# Register your models here.


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ['user', 'bkash_payment', 'mobile_recharge', 'num_of_ref']
    list_filter = ['bkash_payment', 'mobile_recharge']
    search_fields = ['user', 'bkash_num']
    list_per_page = 30


class FreeReferenceAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'ref_code',
                    'bkash_payment', 'mobile_recharge', 'num_of_ref']
    list_filter = ['bkash_payment', 'mobile_recharge']
    search_fields = ['user', 'bkash_num', 'pn_number', 'ref_code']
    list_per_page = 30


admin.site.register(Reference, ReferenceAdmin)
admin.site.register(FreeReference, FreeReferenceAdmin)

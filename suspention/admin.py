from django.contrib import admin
from .models import SuspentionPermanently, SuspentionTemporary
# Register your models here.


class TemporaryAdmin (admin.ModelAdmin):
    list_display = ['user', 'start_month', 'num_of_month', 'approve']
    ordering = ['approve', ]
    search_fields = ['user', ]
    list_per_page = 30


class PermanentlyAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_done', 'device_collect_at']
    ordering = ['is_done', ]
    search_fields = ['user', ]
    list_per_page = 30


admin.site.register(SuspentionTemporary, TemporaryAdmin)
admin.site.register(SuspentionPermanently, PermanentlyAdmin)

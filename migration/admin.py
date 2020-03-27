from django.contrib import admin
from .models import Downgrade, Upgrade

# Register your models here.


class UpgradeAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'is_done']
    ordering = ['is_done', ]
    search_fields = ['user', ]
    list_per_page = 50


class DowngradeAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'is_paid', 'is_done']
    list_filter = ['is_done', 'is_paid']
    ordering = ['is_done', ]
    search_fields = ['user', ]
    list_per_page = 50


admin.site.register(Downgrade, DowngradeAdmin)
admin.site.register(Upgrade, UpgradeAdmin)

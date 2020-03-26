from django.contrib import admin
from .models import ConnectionShift

# Register your models here.


class ConnectionShiftAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_done', 'distic', 'thana', 'created_at']
    list_filter = ['distic', 'thana', 'is_done']
    ordering = ['is_done', ]
    search_fields = ['user', 'distic', 'thana']
    list_per_page = 30


admin.site.register(ConnectionShift, ConnectionShiftAdmin)

from django.contrib import admin
from .models import Task
from django.utils.html import format_html


# Register your models here.



@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status_badge', 'completed', 'created')
    list_display_links = ('title',)
    list_editable = ('completed',)
    list_filter = ('completed',)
    search_fields = ('title',)
    ordering = ('-created',)

    def status_badge(self, obj):
        if obj.completed:
            return format_html('<span style="color: green;">✅ Done</span>')
        return format_html('<span style="color: red;">❌ Pending</span>')

    status_badge.short_description = 'Status'



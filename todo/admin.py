from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    """Custom admin configuration for displaying and managing Todo objects in the admin panel."""
    list_display = ('title', 'user', 'status', 'created_at', 'photo')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'user__username')
    ordering = ('-created_at',)


admin.site.register(Todo, TodoAdmin)

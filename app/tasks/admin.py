from django.contrib import admin
from .models import Task, Tag

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'deadline', 'is_done')
    list_filter = ('is_done',)
    search_fields = ('content',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)

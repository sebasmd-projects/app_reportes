from django.contrib import admin

from apps.registros.models import RegistroModel

# Register your models here.
@admin.register(RegistroModel)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'updated')
    list_display_links = ('id', 'title')
    readonly_fields = ('created', 'updated')
    ordering = ('order', 'id', 'title')
    search_fields = ('id', 'title', 'created', 'updated')
from django.contrib import admin

from apps.usuarios.models import ClientsModel, PublishersModel

# Register your models here.
@admin.register(ClientsModel)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'created', 'updated')
    list_display_links = ('id', 'first_name', 'last_name', 'email')
    readonly_fields = ('full_name', 'age','created', 'updated')
    ordering = ('order', 'id', 'first_name')
    search_fields = ('id', 'first_name', 'created', 'updated')
    
@admin.register(PublishersModel)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_active', 'email', 'created', 'updated')
    list_display_links = ('id', 'first_name', 'last_name', 'email')
    readonly_fields = ('full_name', 'age','created', 'updated')
    ordering = ('order', 'id', 'first_name')
    search_fields = ('id', 'first_name', 'created', 'updated')
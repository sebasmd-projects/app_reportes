from django.contrib import admin

from apps.objetos.models import CategoriesObjectModel, ObjetcModel

# Register your models here.

@admin.register(CategoriesObjectModel)
class CategoriesObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'updated')
    list_display_links = ('id', 'name')
    readonly_fields = ('created', 'updated')
    ordering = ('order', 'id', 'name')
    search_fields = ('id', 'name', 'created', 'updated')

@admin.register(ObjetcModel)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'object_name', 'get_object_category_name', 'created', 'updated')
    list_display_links = ('id', 'object_name', 'get_object_category_name')
    readonly_fields = ('created', 'updated')
    ordering = ('order', 'id', 'object_name')
    search_fields = ('id', 'object_name', 'get_object_category_name', 'created', 'updated')
    
    def get_object_category_name(self, obj):
        return obj.object_category.name
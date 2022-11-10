from django.contrib import admin

from apps.objetos.models import CategoriesObjectModel, ObjetcModel, UseObjectModel

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
    
    
@admin.register(UseObjectModel)
class UseObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_object_name', 'get_user', 'availability', 'created', 'updated')
    list_display_links = ('id', 'get_object_name', 'get_user')
    readonly_fields = ('created', 'updated')
    ordering = ('order', 'id')
    

    def get_object_name(self, obj):
        return obj.object.object_name
    
    def get_user(self, obj):
        return obj.user.full_name
    
    
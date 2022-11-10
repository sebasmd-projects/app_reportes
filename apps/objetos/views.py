from django.views.generic import ListView

from apps.objetos.models import CategoriesObjectModel, ObjetcModel

class ListObjectsByCategoryListView(ListView):
    template_name = 'objetos/list_objects_by_category.html'
    context_object_name = 'objetos'
    
    def get_queryset(self):
        category_id = self.request.GET.get('category_id', '')
        category_name = self.request.GET.get('category_name', '')
        
        return ObjetcModel.objects.search_by_category(category_id, category_name)
    
class ListPublisherByCategoryListView(ListView):
    template_name = 'objetos/list_publisher_by_category.html'
    context_object_name = 'objetos'
    
    def get_queryset(self):
        autor_id = self.request.GET.get('autor_id', '')
        autor_name = self.request.GET.get('autor_name', '')
        
        return CategoriesObjectModel.objects.publisher_by_category(autor_id, autor_name)
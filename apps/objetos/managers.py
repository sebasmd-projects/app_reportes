from django.db import models
from django.db.models import Count, Avg, Sum


class ObjectManager(models.Manager):
    def search_by_category(self, category_id, category_name):

        return self.filter(
            object_category__id__icontains=category_id
        ).filter(
            object_category__name__icontains=category_name
        ).order_by('object_name')
        
    def count_sells(self):
        result = self.aggregate(
            num_sells = Count('object_use')
        )
        return result


class CategoriesObjectManager(models.Manager):
    def publisher_by_category(self, autor_id, autor_name):

        return self.filter(
            # related_name = 'object_category'
            object_category__publisher__full_name__icontains=autor_name
        ).filter(
            object_category__publisher__id__icontains=autor_id
        ).distinct()
        
        """
        shell de Django:
        python manage.py shell
        from apps.objetos.models import *
        CategoriesObjectModel.objects.publisher_by_category("", "Seb")
        <QuerySet [<CategoriesObjectModel: c1>, <CategoriesObjectModel: c2>]>
        exit()
        """
    
    def count_categories_per_object(self):
        # Cuantos objetos tiene una categoria
        result = self.annotate(
            num_objects = Count('object_category')
        ).order_by('num_objects')
        return result
    
    
class UseObjectManager(models.Manager):
    def count_age_per_object(self, object_id, object_name):
        # Promedio de edad por usuario
        result = self.filter(
            object__object_name__icontains=object_name
        ).filter(
            object__id__icontains=object_id
        ).aggregate(
            prom_age = Avg('user__age'),
            sum_age = Sum('user__age')
        )
        
        return result
        

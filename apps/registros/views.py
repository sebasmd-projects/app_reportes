from django.views.generic import TemplateView

from apps.objetos.models import CategoriesObjectModel, ObjetcModel, UseObjectModel


class ReportsTemplateView(TemplateView):
    template_name = 'registros/reportes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registro'
        context['CategoryPerObject'] = CategoriesObjectModel.objects.count_categories_per_object()
        context['UsesPerObject'] = ObjetcModel.objects.count_sells()['num_sells']
        
        object_id = self.request.GET.get('object_id', '')
        object_name = self.request.GET.get('object_name', '')
        context['AvgAgePerObject'] = UseObjectModel.objects.count_age_per_object(object_id, object_name)['prom_age']
        context['SumAgePerObject'] = UseObjectModel.objects.count_age_per_object(object_id, object_name)['sum_age']
        return context


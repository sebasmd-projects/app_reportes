from django.views.generic import (
    View,
    ListView,
    TemplateView
)

from django.shortcuts import render

from apps.usuarios.models import PublishersModel, ClientsModel


class PublisherListView(ListView):
    model = PublishersModel
    template_name = 'usuarios/list_publishers.html'
    context_object_name = 'editores'


class ActivePublisherListView(ListView):
    template_name = 'usuarios/list_publishers.html'
    context_object_name = 'editores'

    def get_queryset(self):
        return PublishersModel.objects.list_is_active()


class FilterPublisherListView(ListView):
    template_name = 'usuarios/filter_list_publishers.html'
    context_object_name = 'editores'

    def get_queryset(self):
        """ 
            El kword es el mismo que debe aparecer en el formulario (plantilla html)
            en el atributo name
            
            El .get('kword','') es para que no de error si no se envia nada en el formulario
        """
        nombres = self.request.GET.get('nombres', '')
        correo = self.request.GET.get('correo', '')
        fecha1 = self.request.GET.get('fecha1', '')
        fecha2 = self.request.GET.get('fecha2', '')
        edad = self.request.GET.get('edad', '')
        id_autor = self.request.GET.get('id_autor', '')
        
        if fecha1 and fecha2:
            resultado = PublishersModel.objects.search_publisher_date(nombres, correo, edad, id_autor, fecha1, fecha2)
        else:
            resultado = PublishersModel.objects.search_publisher(nombres, correo, edad, id_autor)
        return resultado


class ClientsListView(ListView):
    model = ClientsModel
    template_name = 'usuarios/list_clients.html'
    context_object_name = 'clientes'


class ActiveClientsListView(ListView):
    template_name = 'usuarios/list_clients.html'
    context_object_name = 'clientes'

    def get_queryset(self):
        return ClientsModel.objects.list_is_active()


class UsersTemplateView(TemplateView):
    template_name = 'usuarios/list_model_users.html'

    def get_context_data(self, **kwargs):
        ctx = super(UsersTemplateView, self).get_context_data(**kwargs)
        ctx['editores'] = PublishersModel.objects.list_is_active()
        ctx['clientes'] = ClientsModel.objects.list_is_active()
        return ctx


class UsersView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'editores': PublishersModel.objects.list_is_active(),
            'clientes': ClientsModel.objects.list_is_active()
        }
        return render(request, 'usuarios/list_users.html', context)

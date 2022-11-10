from django.urls import path

from apps.usuarios.views import(
    PublisherListView, 
    ClientsListView,  
    UsersView, 
    UsersTemplateView,
    ActivePublisherListView,
    ActiveClientsListView,
    FilterPublisherListView
) 

app_name = 'usuarios'

urlpatterns = [
    path(
        'editores/',
        PublisherListView.as_view(),
        name='publishers'
    ),
    path(
        'editores-activos/',
        ActivePublisherListView.as_view(),
        name='active-publishers'
    ),
    path(
        'filtro-editores/',
        FilterPublisherListView.as_view(),
        name='filter-publishers'
    ),
    path(
        'clientes/',
        ClientsListView.as_view(),
        name='clients'
    ),
    path(
        'clientes-activos/',
        ActiveClientsListView.as_view(),
        name='active-clients'
    ),
    path(
        'usuarios-view/',
        UsersView.as_view(),
        name='users-view'
    ),
    path(
        'usuarios-templateview/',
        UsersTemplateView.as_view(),
        name='users-templateview'
    ),
]

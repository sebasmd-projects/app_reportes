from django.urls import path

from apps.objetos.views import ListObjectsByCategoryListView, ListPublisherByCategoryListView

app_name = 'objetos'

urlpatterns = [
    path(
        'listar-objetos-por-categoria/',
        ListObjectsByCategoryListView.as_view(),
        name='list-objects-by-category'
    ),
    path(
        'listar-editores-por-categoria/',
        ListPublisherByCategoryListView.as_view(),
        name='list-publishers-by-category'
    ),
]

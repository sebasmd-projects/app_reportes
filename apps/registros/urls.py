from django.urls import path

from apps.registros.views import ReportsTemplateView

app_name = 'registros'


urlpatterns = [
    path(
        '',
        ReportsTemplateView.as_view(),
        name='reports'
    ),
]

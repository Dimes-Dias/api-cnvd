from django.urls import path

from .views import AudienciasViewSet, DespachosViewSet, ManifestacoesViewSet

app_name = 'produtividade'

urlpatterns = [
    path(
        'audiencias/v1',
        AudienciasViewSet.as_view({'get': 'list'}),
        name='audiencias'
    ),
    path(
        'despachos/v1',
        DespachosViewSet.as_view({'get': 'list'}),
        name='despachos'
    ),
    path(
        'manifestacoes/v1',
        ManifestacoesViewSet.as_view({'get': 'list'}),
        name='manifestacoes'
    ),
]

from django.urls import path

from .views import (DespachosLocalViewSet, DespachosPeriodoViewSet,
                    DespachosTotaisViewSet, DespachosUsuarioViewSet)

app_name = 'produtividade'

urlpatterns = [
    path(
        'despachos/totais/v1',
        DespachosTotaisViewSet.as_view({'get': 'list'}),
        name='despachos-totais'
    ),
    path(
        'despachos/periodo/v1',
        DespachosTotaisViewSet.as_view({'get': 'list'}),
        name='despachos-periodo'
    ),
    path(
        'despachos/locais/v1',
        DespachosLocalViewSet.as_view({'get': 'list'}),
        name='despachos-locais'
    ),
]

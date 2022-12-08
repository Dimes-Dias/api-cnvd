from django.urls import path

from .views import (ClasseLocalViewSet, ClassesLocaisAPIView, ClasseViewSet,
                    LocalViewSet, ProcessoEnviadoViewSet, ProcessoErroViewSet,
                    TotalViewSet)

app_name = 'cnvd'

urlpatterns = [

    # TOTAIS ------------------------------------------------------
    # resumo dos totais de processos enviados e com erro
    path(
        'totais/v1',
        TotalViewSet.as_view({'get': 'list'}),
        name='totais'
    ),

    # PROCESSOS COM ERRO ------------------------------------------
    # lista de processos com erro
    path(
        'processos/erro/v1',
        ProcessoErroViewSet.as_view({'get': 'list'}),
        name='processos'
    ),
    # lista de processos com erro por local
    path(
        'processos/erro/local/<int:local_pk>/v1',
        ProcessoErroViewSet.as_view({'get': 'list'}),
        name='processos-filter'
    ),

    # PROCESSOS ENVIADOS ------------------------------------------
    # lista completa de processos enviados
    path(
        'processos/enviados/v1',
        ProcessoEnviadoViewSet.as_view({'get': 'list'}),
        name='processos'
    ),
    # lista de processos enviados por local
    path(
        'processos/enviados/local/<int:local_pk>/v1',
        ProcessoEnviadoViewSet.as_view({'get': 'list'}),
        name='processos-filter'
    ),

    # LOCAIS ------------------------------------------------------
    # lista de locais com totais de processos enviados e com erro
    path(
        'locais/v1',
        LocalViewSet.as_view({'get': 'list'}),
        name='locais'
    ),
    path(
        'locais/<int:local_pk>/v1',
        LocalViewSet.as_view({'get': 'list'}),
        name='locais'
    ),
    path(
        'locaisdrilldown/v1',
        ClasseLocalViewSet.as_view({'get': 'list'}),
        name='locais-drilldown'
    ),
    path(
        'classeslocais/v1',
        ClassesLocaisAPIView.as_view(),
        name='classes-locais'
    ),

    # CLASSES -----------------------------------------------------
    # classes de erro com totais
    path(
        'classes/v1',
        ClasseViewSet.as_view({'get': 'list'}),
        name='classes'
    ),
    # classes de erro com totais, por local
    # path(
    #     'classes/local/<int:local_pk>/v1',
    #     ClasseViewSet.as_view({'get': 'list'}),
    #     name='classes-filter'
    # ),

    # STATUS -----------------------------------------------------
    # status de erro com totais
    # path(
    #     'status/v1',
    #     StatusViewSet.as_view({'get': 'list'}),
    #     name='status'
    # ),
    # status de erro com totais, por local
    # path(
    #     'status/local/<int:local_pk>/v1',
    #     StatusViewSet.as_view({'get': 'list'}),
    #     name='status-filter'
    # ),

]

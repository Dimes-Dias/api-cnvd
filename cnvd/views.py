from rest_framework import viewsets

from sgbd.sql import (CLASSE_SQL, CLASSE_SQL_FILTER, LOCAL_SQL,
                      PROCESSO_ENV_SQL, PROCESSO_ENV_SQL_FILTER,
                      PROCESSO_ERRO_SQL, PROCESSO_ERRO_SQL_FILTER, STATUS_SQL,
                      STATUS_SQL_FILTER, TOTAL_SQL)

from .models import Classe, Local, Processo, Status, Total
from .serializers import (ClasseSerializer, LocalSerializer,
                          ProcessoSerializer, StatusSerializer,
                          TotalSerializer)


class TotalViewSet(viewsets.ModelViewSet):

    try:
        queryset = Total.objects.raw(TOTAL_SQL)
    except Exception as e:  # noqa F841
        queryset = None

    serializer_class = TotalSerializer
    pagination_class = None


class LocalViewSet(viewsets.ModelViewSet):

    try:
        queryset = Local.objects.raw(LOCAL_SQL)
    except Exception as e:  # noqa F841
        queryset = None

    serializer_class = LocalSerializer


class ClasseViewSet(viewsets.ModelViewSet):

    serializer_class = ClasseSerializer
    pagination_class = None

    def get_queryset(self):

        if self.kwargs.get('local_pk'):
            try:
                return Classe.objects.raw(
                    CLASSE_SQL_FILTER, [self.kwargs.get('local_pk')]
                )
            except Exception as e:  # noqa F841
                return None

        try:
            return Classe.objects.raw(CLASSE_SQL)
        except Exception as e:  # noqa F841
            return None


class StatusViewSet(viewsets.ModelViewSet):

    serializer_class = StatusSerializer
    pagination_class = None

    def get_queryset(self):

        if self.kwargs.get('local_pk'):
            try:
                return Status.objects.raw(
                    STATUS_SQL_FILTER, [self.kwargs.get('local_pk')]
                )
            except Exception as e:  # noqa F841
                return None

        try:
            return Status.objects.raw(STATUS_SQL)
        except Exception as e:  # noqa F841
            return None


class ProcessoErroViewSet(viewsets.ModelViewSet):

    serializer_class = ProcessoSerializer

    def get_queryset(self):

        if self.kwargs.get('local_pk'):
            try:
                return Processo.objects.raw(
                    PROCESSO_ERRO_SQL_FILTER, [self.kwargs.get('local_pk')]
                )
            except Exception as e:  # noqa F841
                return None

        try:
            return Processo.objects.raw(PROCESSO_ERRO_SQL)
        except Exception as e:  # noqa F841
            return None


class ProcessoEnviadoViewSet(viewsets.ModelViewSet):

    serializer_class = ProcessoSerializer

    def get_queryset(self):

        if self.kwargs.get('local_pk'):
            try:
                return Processo.objects.raw(
                    PROCESSO_ENV_SQL_FILTER, [self.kwargs.get('local_pk')]
                )
            except Exception as e:  # noqa F841
                return None

        try:
            return Processo.objects.raw(PROCESSO_ENV_SQL)
        except Exception as e:  # noqa F841
            return None

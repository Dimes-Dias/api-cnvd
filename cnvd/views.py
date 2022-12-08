from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from sgbd.sql_cnvd import (CLASSE_SQL, LOCAL_SQL, LOCAL_SQL_FILTER,
                           PROCESSO_ENV_SQL, PROCESSO_ENV_SQL_FILTER,
                           PROCESSO_ERRO_SQL, PROCESSO_ERRO_SQL_FILTER,
                           TOTAL_SQL)

from .models import Classe, Local, Processo, Total
from .serializers import (ClasseLocalSerializer, ClasseSerializer,
                          LocalSerializer, ProcessoSerializer, TotalSerializer)


class TotalViewSet(viewsets.ModelViewSet):

    try:
        queryset = Total.objects.raw(TOTAL_SQL)
    except Exception as e:  # noqa F841
        queryset = ''

    serializer_class = TotalSerializer
    pagination_class = None


class LocalViewSet(viewsets.ModelViewSet):

    serializer_class = LocalSerializer
    pagination_class = None

    def get_queryset(self):

        if self.kwargs.get('local_pk'):
            try:
                return Local.objects.raw(
                    LOCAL_SQL_FILTER, [self.kwargs.get('local_pk')]
                )
            except Exception as e:  # noqa F841
                return ''

        try:
            return Local.objects.raw(LOCAL_SQL)
        except Exception as e:  # noqa F841
            return ''


class ClasseViewSet(viewsets.ModelViewSet):

    try:
        queryset = Classe.objects.raw(CLASSE_SQL)
    except Exception as e:  # noqa F841
        queryset = ''

    serializer_class = ClasseSerializer
    pagination_class = None


class ClasseLocalViewSet(viewsets.ModelViewSet):

    try:
        queryset = Classe.objects.raw(CLASSE_SQL)
    except Exception as e:  # noqa F841
        queryset = ''

    serializer_class = ClasseLocalSerializer
    pagination_class = None


class ClassesLocaisAPIView(APIView):

    def get(self, request):

        classe = Classe.objects.raw(CLASSE_SQL)
        sclasse = ClasseSerializer(classe, many=True)
        slocal = ClasseLocalSerializer(classe, many=True)
        data = {'classes': sclasse.data, 'locais': slocal.data}

        return Response(data)


# class StatusViewSet(viewsets.ModelViewSet):

#     serializer_class = StatusSerializer
#     pagination_class = None

#     def get_queryset(self):

#         if self.kwargs.get('local_pk'):
#             try:
#                 return Status.objects.raw(
#                     STATUS_SQL_FILTER, [self.kwargs.get('local_pk')]
#                 )
#             except Exception as e:  # noqa F841
#                 return ''

#         try:
#             return Status.objects.raw(STATUS_SQL)
#         except Exception as e:  # noqa F841
#             return ''


class ProcessoErroViewSet(viewsets.ModelViewSet):

    serializer_class = ProcessoSerializer

    def get_queryset(self):

        if self.kwargs.get('local_pk'):
            try:
                return Processo.objects.raw(
                    PROCESSO_ERRO_SQL_FILTER, [self.kwargs.get('local_pk')]
                )
            except Exception as e:  # noqa F841
                return ''

        try:
            return Processo.objects.raw(PROCESSO_ERRO_SQL)
        except Exception as e:  # noqa F841
            return ''


class ProcessoEnviadoViewSet(viewsets.ModelViewSet):

    serializer_class = ProcessoSerializer

    def get_queryset(self):

        if self.kwargs.get('local_pk'):
            try:
                return Processo.objects.raw(
                    PROCESSO_ENV_SQL_FILTER, [self.kwargs.get('local_pk')]
                )
            except Exception as e:  # noqa F841
                return ''

        try:
            return Processo.objects.raw(PROCESSO_ENV_SQL)
        except Exception as e:  # noqa F841
            return ''

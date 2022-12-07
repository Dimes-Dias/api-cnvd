from datetime import datetime

from rest_framework import viewsets

from sgbd.sql_produtividade import (DESPACHOS_LOCAL_SQL, DESPACHOS_PERIODO_SQL,
                                    DESPACHOS_TOTAIS_SQL,
                                    DESPACHOS_USUARIO_SQL)

from .models import Movimento
from .serializers import MovimentoSerializer


# para evitar erros de aspas sobrando no sql
def remove_aspas(st):
    st = st.replace('"', '')
    st = st.replace("'", '')
    return st


# recebe o parâmetro da url
def recebe_parametro(self, nome_parametro):
    # recebe_dado = self.request.query_params.get(nome_parametro, '')
    recebe_dado = self.request.GET.get(nome_parametro, '').strip()
    recebe_dado = remove_aspas(recebe_dado)
    return recebe_dado


# verifica se as datas foram informadas e se é um período válido (até 2 anos)
# 731 dias considerando a possibilidade de ano bissexto
def intervalo_de_dias(data_inicio, data_fim):
    if (data_inicio != '') and (data_fim != ''):
        recebe_data_inicio = datetime.strptime(
            data_inicio, '%d/%m/%Y').date()
        recebe_data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()
        quantidade_de_dias = (recebe_data_fim - recebe_data_inicio).days
        return (quantidade_de_dias <= 731)
    return False


# faz os ajustes no sql, conforme os filtros passados pela url
def aplica_sql(sql, data_inicio, data_fim, id_local, id_usuario):
    # aplica filtro de datas
    sql = sql.replace('#DATA_INICIO#', data_inicio)
    sql = sql.replace('#DATA_FIM#', data_fim)
    # aplica filtro de local por id
    if id_local == 'todos' or id_local == '':
        id_local = chr(37)+chr(37)
    sql = sql.replace('#ID_LOCAL#', id_local)
    # aplica filtro de responsável por id
    if id_usuario == 'todos' or id_usuario == '':
        id_usuario = chr(37)+chr(37)
    sql = sql.replace('#ID_USUARIO#', id_usuario)
    return sql


class BaseViewSet(viewsets.ModelViewSet):

    serializer_class = MovimentoSerializer
    sql = ''

    def get_queryset(self):
        # recebe as datas do filtro
        data_inicio = recebe_parametro(self, 'data_inicio')
        data_fim = recebe_parametro(self, 'data_fim')

        # verifica se as datas foram de fato informadas e se
        # estão num intervalo de tempo aceitável (2 anos)
        if intervalo_de_dias(data_inicio, data_fim):

            # recebe os demais parâmetros opcionais
            id_local = recebe_parametro(self, 'id_local')
            id_usuario = recebe_parametro(self, 'id_usuario')

            # aplica os filtros à estrutura sql e retorna o resultado
            # da consulta
            try:
                return Movimento.objects.raw(aplica_sql(
                    self.sql,
                    data_inicio,
                    data_fim,
                    id_local,
                    id_usuario
                ))
            except Exception as e:  # noqa F841
                return ''

        return ''


class DespachosTotaisViewSet(BaseViewSet):
    sql = DESPACHOS_TOTAIS_SQL


class DespachosPeriodoViewSet(BaseViewSet):
    sql = DESPACHOS_PERIODO_SQL


class DespachosLocalViewSet(BaseViewSet):
    sql = DESPACHOS_LOCAL_SQL


class DespachosUsuarioViewSet(BaseViewSet):
    sql = DESPACHOS_USUARIO_SQL

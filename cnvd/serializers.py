from rest_framework import serializers

from sgbd.sql_cnvd import CLASSE_LOCAL_SQL

from .models import Classe, ClasseLocal, Local, Processo, Status, Total


# o ModelSerializer codifica/decodifica dados do model DadosEnviados
# em formato JSON de forma automática
class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = '__all__'


class LocalSerializer(serializers.ModelSerializer):

    data = serializers.SerializerMethodField()

    class Meta:
        model = Local
        fields = 'id', 'name', 'data',

    def get_data(self, obj):
        return [obj.total_enviados, obj.total_erros]


class ClasseSerializer(serializers.ModelSerializer):

    drilldown = serializers.SerializerMethodField()
    y = serializers.SerializerMethodField()

    class Meta:
        model = Classe
        fields = 'name', 'y', 'drilldown',

    def get_y(self, obj):
        return obj.erros

    def get_drilldown(self, obj):
        return obj.id


class LocaisSerializer(serializers.ModelSerializer):

    y = serializers.SerializerMethodField()

    class Meta:
        model = ClasseLocal
        fields = 'name', 'y',

    def get_y(self, obj):
        return obj.erros


class ClasseLocalSerializer(serializers.ModelSerializer):

    id = serializers.SerializerMethodField()
    data = serializers.SerializerMethodField()

    class Meta:
        model = Classe
        fields = 'name',  'id',  'data',

    def get_id(self, obj):
        return obj.id

    def get_data(self, obj):
        cl = ClasseLocal.objects.raw(CLASSE_LOCAL_SQL, [obj.id])
        return LocaisSerializer(
            cl,
            many=True
        ).data


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = 'total_enviados', 'total_erros', 'total_geral'

from rest_framework import serializers

from .models import Classe, Local, LocalDrillDown, Processo, Status, Total


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

    y = serializers.SerializerMethodField()
    id = serializers.SerializerMethodField()

    class Meta:
        model = Classe
        fields = 'name', 'y', 'id',

    def get_y(self, obj):
        return obj.erros

    def get_id(self, obj):
        return obj.name


class LocalDrillDownSerializer(serializers.ModelSerializer):

    y = serializers.SerializerMethodField()

    class Meta:
        model = LocalDrillDown
        fields = 'drilldown', 'name', 'y',

    def get_y(self, obj):
        return obj.erros


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = 'total_enviados', 'total_erros', 'total_geral'

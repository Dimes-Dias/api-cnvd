from rest_framework import serializers

from .models import Classe, Local, Processo, Status, Total


# o ModelSerializer codifica/decodifica dados do model DadosEnviados
# em formato JSON de forma automática
class ProcessoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processo
        fields = '__all__'


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = '__all__'


class ClasseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classe
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = 'total_enviados', 'total_erros', 'total_geral'

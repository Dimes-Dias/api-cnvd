from rest_framework import serializers

from .models import Local, Movimento, Periodo, Total, Usuario


class TotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total
        fields = 'total',


class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = 'ano', 'mes', 'total',


class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = 'id_local', 'nome_local', 'total',


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = 'id_usuario', 'nome_usuario', 'total',


class MovimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimento
        fields = 'id_local', 'nome_local', 'id_usuario', \
                 'nome_usuario', 'ano', 'mes', 'total'

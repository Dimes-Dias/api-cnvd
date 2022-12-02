from rest_framework import serializers

from .models import Movimento


class MovimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimento
        fields = 'id_local', 'nome_local', 'id_responsavel', \
                 'nome_responsavel', 'ano', 'mes', 'total'

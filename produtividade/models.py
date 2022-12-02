from django.db import models


class Movimento(models.Model):
    id = models.IntegerField(primary_key=True)
    id_local = models.BigIntegerField()
    nome_local = models.CharField(max_length=120)
    id_responsavel = models.CharField(max_length=15)
    nome_responsavel = models.CharField(max_length=96)
    ano = models.IntegerField()
    mes = models.IntegerField()
    total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'movimento'
        app_label = 'produtividade'

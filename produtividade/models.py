from django.db import models


class Total(models.Model):
    id = models.IntegerField(primary_key=True)
    total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'total'
        app_label = 'produtividade'


class Periodo(models.Model):
    id = models.IntegerField(primary_key=True)
    ano = models.IntegerField()
    mes = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'periodo'
        app_label = 'produtividade'


class Local(models.Model):
    id = models.IntegerField(primary_key=True)
    id_local = models.IntegerField()
    nome_local = models.CharField(max_length=120)
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'local'
        app_label = 'produtividade'


class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    id_usuario = models.CharField(max_length=15)
    nome_usuario = models.CharField(max_length=96)
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'
        app_label = 'produtividade'


class Movimento(models.Model):
    id = models.IntegerField(primary_key=True)
    id_local = models.BigIntegerField()
    nome_local = models.CharField(max_length=120)
    id_usuario = models.CharField(max_length=15)
    nome_usuario = models.CharField(max_length=96)
    ano = models.IntegerField()
    mes = models.IntegerField()
    total = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'movimento'
        app_label = 'produtividade'

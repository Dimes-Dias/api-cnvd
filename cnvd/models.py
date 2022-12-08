from django.db import models


class Local(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=120)
    total_enviados = models.IntegerField()
    total_erros = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'local'
        app_label = 'cnvd'


class Classe(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    erros = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'classe'
        app_label = 'cnvd'


class ClasseLocal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    # classe = models.ForeignKey(
    #     'Classe', related_name='data', on_delete=models.CASCADE)
    classe = models.IntegerField()
    name = models.CharField(max_length=120)
    erros = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'classelocal'
        app_label = 'cnvd'


class Status(models.Model):
    descricao = models.CharField(primary_key=True, max_length=50)
    erros = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'status'
        app_label = 'cnvd'


class Processo(models.Model):
    cdlogdetalhe = models.BigIntegerField(primary_key=True)
    numero_processo = models.CharField(max_length=255)
    classe = models.CharField(max_length=50)
    mensagem = models.CharField(max_length=255)
    local = models.CharField(max_length=120)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False  # faz o django não mexer na estrutura da tabela
        db_table = '"saj"."efmpresolucao135logdetalhe"'
        app_label = 'cnvd'


class Total(models.Model):
    id = models.IntegerField(primary_key=True)
    total_enviados = models.BigIntegerField()
    total_erros = models.BigIntegerField()
    total_geral = models.BigIntegerField()

    class Meta:
        managed = False  # faz o django não mexer na estrutura da tabela
        db_table = 'total'
        app_label = 'cnvd'

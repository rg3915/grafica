from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    criado_em = models.DateTimeField(
        'criado em',
        auto_now_add=True,
        auto_now=False
    )
    modificado_em = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
    )

    class Meta:
        abstract = True


class SaidaBase(models.Model):
    titulo = models.CharField(max_length=100)
    altura = models.PositiveIntegerField(null=True, blank=True)
    largura = models.PositiveIntegerField(null=True, blank=True)
    recomendacao = models.TextField(null=True, blank=True)
    arquivo = models.FileField(null=True, blank=True)
    criado_por = models.ForeignKey(
        User,
        verbose_name='criado por',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('titulo',)
        abstract = True

    def __str__(self):
        return self.titulo


class Ativo(models.Model):
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Fotolito(SaidaBase, TimeStampedModel, Ativo):
    cores = models.CharField(
        'número de cores',
        max_length=10,
        null=True,
        blank=True
    )
    lineatura = models.ForeignKey(
        'Lineatura',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'fotolito'
        verbose_name_plural = 'fotolitos'


class Lineatura(models.Model):
    lineatura = models.CharField(max_length=5)

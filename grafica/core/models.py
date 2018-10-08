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


class Ativo(models.Model):
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

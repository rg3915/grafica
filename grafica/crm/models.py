from django.db import models
from django.contrib.auth.models import User
from grafica.core.models import Ativo


class UserProfile(User, Ativo):
    '''
    Multi-table inheritance
    Tabela de herança múltipla
    Ele cria uma OneToOneField automaticamente a partir de User.
    No caso, são duas tabelas.
    https://docs.djangoproject.com/en/2.1/topics/db/models/#multi-table-inheritance
    '''
    cpf = models.CharField(
        'CPF',
        max_length=14,
        unique=True,
        null=True,
        blank=True
    )
    rg = models.CharField(
        'RG',
        max_length=20,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('first_name', 'last_name')
        verbose_name = 'perfil'
        verbose_name_plural = 'perfils'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Person(User, Ativo):
    pass

    class Meta:
        abstract = True


class PF(Person):
    rg = models.CharField(max_length=20, blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    birthdate = models.DateField(
        verbose_name='Data de Nascimento',
        blank=True,
        null=True
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'


class PJ(Person):
    company_name = models.CharField(
        max_length=255,
        verbose_name='Razão Social'
    )
    cnpj = models.CharField(max_length=14, null=True, blank=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Pessoa Jurídica'
        verbose_name_plural = 'Pessoas Jurídicas'
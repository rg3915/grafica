from django.db import models


class ClienteManager(models.Manager):

    def get_queryset(self):
        return super(ClienteManager, self).get_queryset().filter(tipo='c')


class FornecedorManager(models.Manager):

    def get_queryset(self):
        return super(FornecedorManager, self).get_queryset().filter(tipo='f')

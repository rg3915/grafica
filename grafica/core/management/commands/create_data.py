from django.core.management.base import BaseCommand
from grafica.crm.models import Cliente
from grafica.utils.gen_random_values import (
    gen_phone, gen_cnpj, gen_full_name, gen_email
)


class Command(BaseCommand):
    help = ''' Cria dados aleatorios e salva no banco. '''

    def handle(self, *args, **kwargs):
        nome = gen_full_name()
        email = gen_email(nome)
        telefone = gen_phone()
        cnpj = gen_cnpj()
        Cliente.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            cnpj=cnpj,
            tipo='c',
        )

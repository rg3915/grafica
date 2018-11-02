import timeit
from django.core.management.base import BaseCommand
from grafica.crm.models import Cliente
from grafica.utils.gen_random_values import (
    gen_phone, gen_cnpj, gen_full_name, gen_email
)


class Command(BaseCommand):
    help = ''' Cria dados aleatorios e salva no banco. '''

    def add_arguments(self, parser):
        parser.add_argument(
            '-r', '--repeat', default=1, help='Quantidade de registros a ser criado.'
        )

    def handle(self, *args, **kwargs):
        tic = timeit.default_timer()
        aux = []
        max_length = kwargs['repeat']
        for i in range(int(max_length)):
            nome = gen_full_name()
            email = gen_email(nome)
            telefone = gen_phone()
            cnpj = gen_cnpj()
            obj = Cliente(
                nome=nome,
                email=email,
                telefone=telefone,
                cnpj=cnpj,
                tipo='c',
            )
            aux.append(obj)
        Cliente.objects.bulk_create(aux)
        toc = timeit.default_timer()
        print(toc - tic)

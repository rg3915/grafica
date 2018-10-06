from django.test import TestCase
from grafica.core.models import Fotolito, Ctp, ProvaDeCor, FineArt


class FotolitoTestCase(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'titulo',
            'altura',
            'largura',
            'cores',
            'lineatura',
            'recomendacao',
            'arquivo',
            'status',
            'criado_por',
            'criado_em',
            'modificado_em',
            'ativo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Fotolito, field))


class CtpTestCase(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'titulo',
            'lineatura',
            'quantidade',
            'formato',
            'opcao',
            'reticula',
            'chapa',
            'recomendacao',
            'arquivo',
            'status',
            'criado_por',
            'criado_em',
            'modificado_em',
            'ativo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Ctp, field))


class ProvaDeCorTestCase(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'titulo',
            'altura',
            'largura',
            'formato',
            'papel',
            'recomendacao',
            'arquivo',
            'status',
            'criado_por',
            'criado_em',
            'modificado_em',
            'ativo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(ProvaDeCor, field))


class FineArtTestCase(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'titulo',
            'altura',
            'largura',
            'quantidade',
            'formato',
            'papel',
            'recomendacao',
            'arquivo',
            'status',
            'criado_por',
            'criado_em',
            'modificado_em',
            'ativo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(FineArt, field))

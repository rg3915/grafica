from django.test import TestCase
from grafica.core.models import Fotolito


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
            'criado_por',
            'criado_em',
            'modificado_em',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(Fotolito, field))

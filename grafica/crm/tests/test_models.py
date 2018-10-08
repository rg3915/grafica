from django.test import TestCase
from grafica.crm.models import UserProfile, PF, PJ


class UserProfileTestCase(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'cpf',
            'rg',
            'ativo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(UserProfile, field))


class PFTestCase(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'rg',
            'cpf',
            'birthdate',
            'ativo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(PF, field))


class PJTestCase(TestCase):

    def test_should_return_attributes(self):
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'company_name',
            'cnpj',
            'ativo',
        )

        for field in fields:
            with self.subTest():
                self.assertTrue(hasattr(PJ, field))

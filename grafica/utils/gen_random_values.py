import names
import string
from random import choice
from django.utils.text import slugify


def gen_digits(max_length):
    return str(''.join(choice(string.digits) for i in range(max_length)))


def gen_phone():
    phone = '({}) {}-{}'.format(gen_digits(2), gen_digits(5), gen_digits(4))
    return phone


def gen_cnpj():
    cnpj = gen_digits(14)
    return cnpj


def gen_full_name():
    return names.get_full_name()


def gen_email(name):
    _name = slugify(name)
    email = '{}@email.com'.format(_name)
    return email

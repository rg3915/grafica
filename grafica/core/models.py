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
    quantidade = models.PositiveIntegerField(null=True, blank=True)
    formato = models.ForeignKey(
        'Formato',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    recomendacao = models.TextField(null=True, blank=True)
    arquivo = models.FileField(null=True, blank=True)
    criado_por = models.ForeignKey(
        User,
        verbose_name='criado por',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    STATUS_CHOICES = (
        ('abe', 'Aberto'),
        ('rec', 'Recebido'),
        ('pro', 'Produção'),
        ('fin', 'Finalizado'),
        ('sai', 'Saída'),
        ('ent', 'Entregue'),
    )
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='abe'
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
    PERSON_TYPE= (
        ('PF','Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    )
    person_type = models.CharField(
        max_length=2, 
        choices=PERSON_TYPE,
        blank=True,
        null=True,
        )

    class Meta:
        abstract = True


class PersonPF(Person):
    name = Person.username
    rg = models.CharField(max_length=255, blank = True, null = True)
    cpf = models.CharField(max_length=255, blank = True, null = True)
    birthdate = models.DateField(verbose_name='Data de Nascimento', blank = True, null = True)

    # def __str__(self):
    #     return self.name
    
    class Meta:
        verbose_name = 'Cadastro Pessoa Física'
        verbose_name_plural = 'Cadastro de Pessoas Físicas'
        # ordering = name

class PersonPJ(Person):
    company_name = models.CharField(max_length = 255, verbose_name = 'Razão Social')
    cnpj = models.CharField(max_length = 255)

    def __str__(self):
        return self.company_name
    
    class Meta:
        verbose_name = 'Cadastro Pessoa Jurídica'
        verbose_name_plural = 'Cadastro de Pessoas Jurídicas'


class Lineatura(models.Model):
    titulo = models.CharField(max_length=5)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'lineatura'
        verbose_name_plural = 'lineaturas'

    def __str__(self):
        return self.titulo


class Formato(models.Model):
    titulo = models.CharField(max_length=10)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'formato'
        verbose_name_plural = 'formatos'

    def __str__(self):
        return self.titulo


class Papel(models.Model):
    titulo = models.CharField(max_length=50)

    class Meta:
        ordering = ('titulo',)
        verbose_name = 'papel'
        verbose_name_plural = 'papéis'

    def __str__(self):
        return self.titulo


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


class Ctp(SaidaBase, TimeStampedModel, Ativo):
    lineatura = models.ForeignKey(
        'Lineatura',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    opcao = models.TextField('opção', null=True, blank=True)
    RETICULA_CHOICES = (
        ('con', 'convencional'),
        ('sub', 'sublimática'),
        ('est', 'estocástica'),
    )
    reticula = models.CharField(
        'retícula',
        max_length=3,
        choices=RETICULA_CHOICES,
        default='con'
    )
    chapa = models.BooleanField('chapas forneadas', default=False)

    class Meta:
        verbose_name = 'CTP'
        verbose_name_plural = 'CTPs'


class ProvaDeCor(SaidaBase, TimeStampedModel, Ativo):
    papel = models.ForeignKey(
        'Papel',
        verbose_name='papéis',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Prova de Cor'
        verbose_name_plural = 'Provas de Cor'


class FineArt(SaidaBase, TimeStampedModel, Ativo):
    papel = models.ForeignKey(
        'Papel',
        verbose_name='papéis',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'FineArt'
        verbose_name_plural = 'FineArts'

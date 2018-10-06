# Generated by Django 2.1.2 on 2018-10-06 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_fotolito_ativo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ctp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('titulo', models.CharField(max_length=100)),
                ('altura', models.PositiveIntegerField(blank=True, null=True)),
                ('largura', models.PositiveIntegerField(blank=True, null=True)),
                ('quantidade', models.PositiveIntegerField(blank=True, null=True)),
                ('recomendacao', models.TextField(blank=True, null=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='')),
                ('ativo', models.BooleanField(default=True)),
                ('opcao', models.TextField(blank=True, null=True, verbose_name='opção')),
                ('reticula', models.CharField(default='con', max_length=3, verbose_name='retícula')),
                ('chapa', models.BooleanField(default=False, verbose_name='chapas forneadas')),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
            ],
            options={
                'verbose_name': 'fotolito',
                'verbose_name_plural': 'fotolitos',
            },
        ),
        migrations.CreateModel(
            name='Formato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formato', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='fotolito',
            name='quantidade',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ctp',
            name='formato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Formato'),
        ),
        migrations.AddField(
            model_name='ctp',
            name='lineatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Lineatura'),
        ),
        migrations.AddField(
            model_name='fotolito',
            name='formato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Formato'),
        ),
    ]

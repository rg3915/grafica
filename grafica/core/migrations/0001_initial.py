# Generated by Django 2.1.2 on 2018-10-06 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotolito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('altura', models.PositiveIntegerField(blank=True, null=True)),
                ('largura', models.PositiveIntegerField(blank=True, null=True)),
                ('cores', models.CharField(blank=True, max_length=10, null=True, verbose_name='número de cores')),
                ('recomendacao', models.TextField(blank=True, null=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modificado_em', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='criado por')),
            ],
            options={
                'verbose_name': 'fotolito',
                'verbose_name_plural': 'fotolitos',
                'ordering': ('titulo',),
            },
        ),
        migrations.CreateModel(
            name='Lineatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineatura', models.CharField(max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='fotolito',
            name='lineatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Lineatura'),
        ),
    ]

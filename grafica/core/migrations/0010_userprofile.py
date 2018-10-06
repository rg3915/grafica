# Generated by Django 2.1.2 on 2018-10-06 19:32

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('core', '0009_auto_20181006_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('ativo', models.BooleanField(default=True)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=20, null=True, verbose_name='RG')),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfils',
                'ordering': ('first_name', 'last_name'),
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

# Generated by Django 2.1.2 on 2018-10-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181006_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotolito',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
    ]

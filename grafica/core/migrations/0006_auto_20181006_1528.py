# Generated by Django 2.1.2 on 2018-10-06 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181006_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formato',
            old_name='formato',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='lineatura',
            old_name='lineatura',
            new_name='titulo',
        ),
        migrations.RenameField(
            model_name='papel',
            old_name='papel',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='ctp',
            name='papel',
        ),
        migrations.RemoveField(
            model_name='fotolito',
            name='papel',
        ),
    ]

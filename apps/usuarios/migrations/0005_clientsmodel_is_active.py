# Generated by Django 4.1.3 on 2022-11-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_publishersmodel_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsmodel',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-10 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_clientsmodel_age_alter_publishersmodel_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsmodel',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='publishersmodel',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Edad'),
        ),
    ]

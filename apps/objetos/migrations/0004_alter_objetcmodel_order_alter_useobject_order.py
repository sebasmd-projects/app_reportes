# Generated by Django 4.1.3 on 2022-11-09 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objetos', '0003_alter_categoriesobjectmodel_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetcmodel',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='useobject',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Orden'),
        ),
    ]

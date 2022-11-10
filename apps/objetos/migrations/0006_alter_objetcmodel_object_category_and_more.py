# Generated by Django 4.1.3 on 2022-11-10 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_alter_clientsmodel_created_and_more'),
        ('objetos', '0005_alter_categoriesobjectmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objetcmodel',
            name='object_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object_category', to='objetos.categoriesobjectmodel'),
        ),
        migrations.RemoveField(
            model_name='objetcmodel',
            name='publisher',
        ),
        migrations.AddField(
            model_name='objetcmodel',
            name='publisher',
            field=models.ManyToManyField(to='usuarios.publishersmodel'),
        ),
    ]

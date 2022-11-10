from django.db import models

from django.utils import timezone

from apps.usuarios.models import ClientsModel, PublishersModel

# Create your models here.


class CategoriesObjectModel(models.Model):
    name = models.CharField(
        "Categoria",
        max_length=50,
        default='none',
    )

    created = models.DateField(
        'Fecha de cración',
        default=timezone.now,
        blank=True, null=True
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        blank=True, null=True
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['order']
        db_table = 'app_category_object'


class ObjetcModel(models.Model):
    object_category = models.ForeignKey(
        CategoriesObjectModel,
        on_delete=models.CASCADE,
    )

    object_name = models.CharField(
        'Nombre del objeto',
        max_length=100
    )
    
    publisher = models.ForeignKey(
        PublishersModel,
        on_delete = models.CASCADE,
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        blank=True, null=True
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        blank=True, null=True
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return self.object_name

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'
        ordering = ['order']
        db_table = 'app_object'


class UseObject(models.Model):
    user = models.ForeignKey(
        ClientsModel,
        on_delete=models.CASCADE,
    )

    object = models.ForeignKey(
        ObjetcModel,
        on_delete=models.CASCADE,
    )

    availability = models.BooleanField(
        'Disponibilidad'
    )

    created = models.DateTimeField(
        'Fecha de cración',
        default=timezone.now,
        blank=True, null=True
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
        blank=True, null=True
    )

    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        blank=True, null=True
    )
    
    def __str__(self):
        return self.object.object_name

    class Meta:
        verbose_name = 'Uso de objeto'
        verbose_name_plural = 'Uso de objetos'
        ordering = ['order']
        db_table = 'app_use_object'

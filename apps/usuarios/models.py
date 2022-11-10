from datetime import date

from django.db import models
from django.utils import timezone

from apps.usuarios.managers import ClientsManager, PublishersManager

# Create your models here.


class UsersModel(models.Model):
    first_name = models.CharField(
        'Nombres',
        max_length=40,
        default='',
    )

    last_name = models.CharField(
        'Apellidos',
        max_length=40,
        default='',
    )

    full_name = models.CharField(
        'Nombre(s) y Apellido(s)',
        max_length=100,
        default='',
    )

    email = models.EmailField(
        'Correo',
        max_length=254,
        unique=True,
    )

    birthday = models.DateField(
        'Fecha de nacimiento',
        default=timezone.now,
        blank=True, null=True
    )

    age = models.IntegerField(
        'Edad',
        default=0,
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

    is_active = models.BooleanField(
        "Activo",
        default=True,
    )

    def save(self, *args, **kwargs):

        self.full_name = f"{self.first_name} {self.last_name}"

        self.age = date.today().year - self.birthday.year - (
            (
                date.today().month, date.today().day
            ) < (
                self.birthday.month, self.birthday.day
            )
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['order']
        abstract = True


class PublishersModel(UsersModel):

    objects = PublishersManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Editor'
        verbose_name_plural = 'Editores'
        ordering = ['order']
        db_table = 'app_publisher'


class ClientsModel(UsersModel):

    objects = ClientsManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['order']
        db_table = 'app_client'

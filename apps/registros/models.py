from django.utils import timezone

from django.db import models

# Create your models here.


class RegistroModel(models.Model):
    
    title = models.CharField(
        'Titulo', 
        max_length = 100,
        default = f'Titulo'
    )
        

    created = models.DateField(
        'Fecha de cración',
        default=timezone.now,
        blank=True, null=True
    )

    updated = models.DateTimeField(
        'Fecha de edición',
        auto_now=True,
    )
    
    order = models.PositiveIntegerField(
        'Orden',
        default=0,
        blank=True, null=True
    )
    
    class Meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'
        db_table = 'apps_registro'
        ordering = ['order', 'id','title']

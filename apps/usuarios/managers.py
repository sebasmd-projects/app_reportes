import datetime

from django.db import models

from django.db.models import Q


"""
    El self es equivalente al PublisherModel.objects
    gt = mayor que
    lt = menor que
    Q() | Q() = OR
    something , something = AND
    .filter().filter().exclude().order_by().distinct()

    .exclude(
        is_superuser=True,
        is_staff=True
    )
    .filter(
        age__gt=18,  # mayor que
        age__lt=100,  # menor que
    )
    .order_by(
        'order',
        'id,
        'first_name'
    )
  
"""


class UsersManager(models.Manager):
    def list_is_active(self):
        return self.exclude(is_active=False)


class PublishersManager(UsersManager):
    def search_publisher(self, nombres, correo, edad, id_autor):

        name = nombres
        email = correo
        age = edad
        id_author = id_autor
        

        return self.filter(
            full_name__icontains=name,
        ).filter(
            email__icontains=email
        ).filter(
            age__icontains= age
        ).filter(
            id__icontains= id_author
        )

    def search_publisher_date(self, nombres, correo, edad, id_autor, fecha1, fecha2):

        name = nombres
        email = correo
        age = edad
        id_author = id_autor

        fecha1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        fecha2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        return self.filter(
            full_name__icontains=name
        ).filter(
            email__icontains=email
        ).filter(
            age__icontains= age
        ).filter(
            id__icontains= id_author
        ).filter(
            created__range=(fecha1, fecha2)
        )


class ClientsManager(UsersManager):
    pass

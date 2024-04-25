from django.db import models
from django.utils.translation import gettext as _
from .models_user import User
from .models_service import Service

class Reservation(models.Model):
    client = models.ForeignKey(
        User,
        related_name='user',
        on_delete=models.CASCADE
    )
    professional = models.ForeignKey(
        User,
        related_name='profesional',
        on_delete=models.CASCADE
    )
    service =models.ManyToManyField(
        Service,
        verbose_name='servicios',
    )
    date = models.DateField()
    datecreate = models.DateField(auto_now=True)
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
USER_ROLES = (
    ('normal','Normal'),
    ('admin','Admin'),
    ('superadmin','SuperAdmin'),
   
)
USER_STATUS = (
    ('active','Active'),
    ('delete','Delete'),
    ('suspended','Suspended'),
   
)

SERVICES_STATUS = (
    ('active','Active'),
    ('delete','Delete'),
    ('stoped','Stoped'),
   
)

class User(models.Model):
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    role =  models.CharField(max_length=10, choices=USER_ROLES, default='normal')
    email = models.EmailField(max_length=500, null=False)
    birthdate = models.DateField()
    datecreate = models.DateField(auto_now=True)
    # pic_profile = models.ImageField(upload_to ='uploads/% Y/% m/% d/')
    password = models.CharField(_('password'), max_length=128)
    status = models.CharField(max_length=10, choices=USER_STATUS, default='active')

class Service(models.Model):
    name = models.CharField(max_length=255, null=False)
    datecreate = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=USER_STATUS, default='active')
    description = models.CharField(max_length=555, null=False)
    price = models.FloatField()
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
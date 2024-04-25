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



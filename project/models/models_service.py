from django.db import models
from django.utils.translation import gettext as _

SERVICES_STATUS = (
    ('active','Active'),
    ('delete','Delete'),
    ('stoped','Stoped'),
)
class Service(models.Model):
    name = models.CharField(max_length=255, null=False)
    datecreate = models.DateField(auto_now=True)
    status = models.CharField(max_length=10, choices=SERVICES_STATUS, default='active')
    description = models.CharField(max_length=555, null=False)
    price = models.FloatField()
    
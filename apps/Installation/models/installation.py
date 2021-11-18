from django.db import models
from django.db.models import base

# Create your models here.
machines=(
        (0,'Granos'),
        (1,'Granos chicos'),
        (2,'Mayor capacidad'),
        (3, 'Maquina estandar')
 )

class Installation (models.Model):
    installation_id = models.BigAutoField(primary_key=True, null=False)
    user_id = models.BigIntegerField("user_id", null=True, blank=False)
    address = models.CharField("Address", max_length=200, null=True, blank=False)
    city = models.CharField("City", max_length=50, null=True)
    machine_type = models.CharField("Machine_type", choices=machines, max_length=50, null=True, blank=False)
    accepted = models.BooleanField("Accepted", default=False)
    response = models.TextField("Response", max_length=600, blank=True, null=True)
    date_create = models.DateField("Date_create", auto_now_add=True)
    date_response = models.DateField("Date_response", auto_now_add=True)
    
    
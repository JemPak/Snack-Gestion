from django.db import models
from django.db.models import base

# Create your models here.
machines=(
        ('Granos','Granos'),
        ('Granos chicos','Granos chicos'),
        ('Mayor capacidad','Mayor capacidad'),
        ('Maquina estandar', 'Maquina estandar')
 )

class Installation (models.Model):
    installation_id = models.BigAutoField(primary_key=True, null=False)
    user_id = models.BigIntegerField("user_id",null=False, blank=False)
    address = models.CharField("Address", max_length=200, null=True, blank=True)
    machine_type = models.CharField("Machine_type", choices=machines, max_length=50, null=False, blank=False)
    accepted = models.BooleanField("Accepted", null=False, blank=False)
    response = models.TextField("Response", max_length=600, blank=True, null=True)
    date_create = models.DateField("Date_create", blank=False, null=False)
    date_response = models.DateField("Date_response", null=False, blank=False)
    
    
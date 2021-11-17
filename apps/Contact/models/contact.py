from django.db import models

# Create your models here.
assesory_type=(
        ('Informacion','Informacion'),
        ('Instalacion','Instalacion'),
        ('Quejas y reclamos','Quejas y reclamos')
 )

class Contact (models.Model):
    contact_id = models.BigAutoField(primary_key=True, null=False)
    user_id = models.BigIntegerField("user_id",null=False, blank=False)
    assesory = models.CharField("Assesory_type", max_length=50, choices=assesory_type, null=False, blank=False)
    comment = models.TextField("Comment", max_length=600, null=True, blank=True)
    is_active = models.BooleanField("is_active", null=False, blank=False)
    response = models.TextField("Response", max_length=600, blank=True, null=True)
    date_create = models.DateField("Date_create", blank=False, null=False)
    date_response = models.DateField("Date_response", null=False, blank=False)


        
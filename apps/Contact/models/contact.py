from django.db import models

# Create your models here.
assesory_type=(
        (0,'Informacion'),
        (1,'Instalacion'),
        (2,'Quejas y reclamos')
 )

class Contact (models.Model):
    contact_id = models.BigAutoField(primary_key=True, null=False)
    user_id = models.BigIntegerField("user_id", null=False, blank=False)
    assesory = models.CharField("Assesory_type", max_length=50, choices=assesory_type, null=True, blank=False)
    comment = models.TextField("Comment", max_length=600, blank=True)
    is_active = models.BooleanField("is_active", default=True)
    response = models.TextField("Response", max_length=600, blank=True, null=True)
    date_create = models.DateField("Date_create", auto_now_add=True)
    date_response = models.DateField("Date_response", null=True) 

        
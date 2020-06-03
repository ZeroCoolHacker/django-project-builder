
from django.db import models

class Car(models.Model):
    
    Make = CharField()
    
    Model = CharField()
    
    Description = TextField()
    

    class Meta:
    """Meta definition for Car."""

    verbose_name = 'Car'
    verbose_name_plural = 'Car'



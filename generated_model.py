
from django.db import models

class Car(models.Model):


    Make = models.CharField(null=False,blank=False)
    Model = models.CharField(null=False,blank=False)
    Description = models.TextField(null=False,blank=False)
    

    class Meta:
        """Meta definition for Car."""

        verbose_name = 'Car'
        verbose_name_plural = 'Car'



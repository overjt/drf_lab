from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre", blank=True, null=True)
    last_name = models.CharField(max_length=100, verbose_name="Apellido", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Fecha de nacimiento", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="Dirección", blank=True, null=True)
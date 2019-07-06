from django.db import models
from persons.models import Person

class Pet(models.Model):
    GENDER_CHOICES = (
        ('M', 'Macho'),
        ('H', 'Hembra'),
    )
    TYPE_CHOICES = (
        ('P', 'Perro'),
        ('G', 'Gato'),
        ('H', 'Hamster'),
        ('B', 'Pájaro'),
        ('O', 'Otro'),
    )
    name = models.CharField(max_length=100, verbose_name="Nombre", blank=True, null=True)
    weight = models.FloatField(verbose_name="Peso", blank=True, null=True)
    color = models.CharField(max_length=30, verbose_name="Color", blank=True, null=True)
    gender = models.CharField(max_length=1, verbose_name="Género", choices=GENDER_CHOICES)
    pet_type = models.CharField(max_length=1, verbose_name="Tipo", choices=TYPE_CHOICES)
    owner = models.ForeignKey(Person, verbose_name="Dueño", on_delete=models.CASCADE)
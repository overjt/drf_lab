# Generated by Django 2.2.3 on 2019-07-06 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellido')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Dirección')),
            ],
        ),
    ]

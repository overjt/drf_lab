# Generated by Django 2.2.3 on 2019-07-06 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Peso')),
                ('color', models.CharField(blank=True, max_length=30, null=True, verbose_name='Color')),
                ('gender', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1, verbose_name='Género')),
                ('pet_type', models.CharField(choices=[('P', 'Perro'), ('G', 'Gato'), ('H', 'Hamster'), ('B', 'Pájaro'), ('O', 'Otro')], max_length=1, verbose_name='Tipo')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Person', verbose_name='Dueño')),
            ],
        ),
    ]

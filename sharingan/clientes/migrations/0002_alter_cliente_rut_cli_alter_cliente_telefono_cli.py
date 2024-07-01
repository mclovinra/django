# Generated by Django 4.2 on 2024-06-30 18:52

import clientes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='rut_cli',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, validators=[clientes.models.validate_only_numbers]),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_cli',
            field=models.CharField(max_length=15, validators=[clientes.models.validate_only_numbers]),
        ),
    ]
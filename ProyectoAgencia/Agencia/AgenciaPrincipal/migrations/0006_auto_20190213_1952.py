# Generated by Django 2.1.5 on 2019-02-13 22:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgenciaPrincipal', '0005_auto_20190213_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='NumeroAsientoAsginado',
            field=models.IntegerField(editable=False, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]

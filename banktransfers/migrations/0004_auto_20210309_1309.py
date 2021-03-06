# Generated by Django 2.2.10 on 2021-03-09 07:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banktransfers', '0003_auto_20210308_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='balance',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]

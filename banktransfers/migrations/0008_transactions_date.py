# Generated by Django 2.2.10 on 2021-03-10 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('banktransfers', '0007_auto_20210309_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2 on 2020-06-14 15:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0002_provider_mobile_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='clinic_contact_no',
            field=models.PositiveIntegerField(blank=True, default=1, validators=[django.core.validators.MaxValueValidator(9999999999)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='provider',
            name='mobile_no',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-17 10:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=16, validators=[django.core.validators.MinLengthValidator(6)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]

# Generated by Django 2.2 on 2020-05-24 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discounts', to='shop.Shop')),
            ],
            options={
                'ordering': ('shop',),
            },
        ),
    ]

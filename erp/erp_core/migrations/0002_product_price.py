# Generated by Django 4.0.2 on 2022-08-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
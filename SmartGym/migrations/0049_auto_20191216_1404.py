# Generated by Django 2.2 on 2019-12-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0048_auto_20191216_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuota',
            name='fecha_vencimiento',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Fecha del Vencimiento'),
        ),
    ]
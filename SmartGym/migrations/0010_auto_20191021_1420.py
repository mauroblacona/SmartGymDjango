# Generated by Django 2.2 on 2019-10-21 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0009_auto_20191021_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='especialidad',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Especialidad'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='observaciones_medicas',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones Medicas'),
        ),
    ]

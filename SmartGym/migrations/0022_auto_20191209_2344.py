# Generated by Django 2.2 on 2019-12-09 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0021_auto_20191209_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caja',
            options={'verbose_name': 'Caja', 'verbose_name_plural': 'Cajas'},
        ),
        migrations.AlterModelOptions(
            name='cuota',
            options={'verbose_name': 'Cuota', 'verbose_name_plural': 'Cuotas'},
        ),
        migrations.AlterModelOptions(
            name='liquidacion',
            options={'verbose_name': 'Liquidacion', 'verbose_name_plural': 'Liquidaciones'},
        ),
        migrations.AlterModelOptions(
            name='recordatorio',
            options={'verbose_name': 'Recordatorio', 'verbose_name_plural': 'Recordatorios'},
        ),
        migrations.AlterModelOptions(
            name='turno',
            options={'verbose_name': 'Turno', 'verbose_name_plural': 'Turnos'},
        ),
    ]

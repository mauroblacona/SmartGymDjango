# Generated by Django 2.2 on 2019-10-11 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0006_auto_20191009_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Hora de Inicio')),
                ('hora_fin', models.DateTimeField(blank=True, null=True, verbose_name='Hora de Fin')),
                ('dia', models.DateField(blank=True, null=True, verbose_name='Dia de la Actividad')),
                ('actividad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Actividad')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
            },
        ),
    ]

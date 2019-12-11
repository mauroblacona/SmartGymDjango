# Generated by Django 2.2 on 2019-12-10 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0036_auto_20191210_2339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='horarioconsultorio',
            options={'verbose_name': 'Horario Consultorio', 'verbose_name_plural': 'Horarios Consultorios'},
        ),
        migrations.AlterField(
            model_name='horarioconsultorio',
            name='dia',
            field=models.CharField(blank=True, choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miercoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sabado', 'Sabado'), ('Domingo', 'Domingo')], max_length=150, null=True, verbose_name='Dia de Atención'),
        ),
    ]

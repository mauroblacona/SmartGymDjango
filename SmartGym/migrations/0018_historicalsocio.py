# Generated by Django 2.2 on 2019-12-04 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SmartGym', '0017_auto_20191204_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSocio',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=120, null=True, verbose_name='Nombres')),
                ('apellido', models.CharField(blank=True, max_length=120, null=True, verbose_name='Apellidos')),
                ('email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico')),
                ('dni', models.IntegerField(blank=True, null=True, verbose_name='Documento')),
                ('genero', models.CharField(blank=True, max_length=50, null=True, verbose_name='Genero')),
                ('telefono', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('telefono_emergencia', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono de Emergencia')),
                ('domicilio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio')),
                ('foto', models.TextField(blank=True, max_length=100, null=True, verbose_name='Foto de Perfil')),
                ('ficha_medica', models.TextField(blank=True, null=True, verbose_name='Ficha Medica')),
                ('saldo', models.BooleanField(blank=True, default=True, null=True, verbose_name='Al dia / Debe')),
                ('observaciones_medicas', models.TextField(blank=True, null=True, verbose_name='Observaciones Medicas')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Socio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
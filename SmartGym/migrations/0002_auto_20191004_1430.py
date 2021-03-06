# Generated by Django 2.2 on 2019-10-04 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='dni',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='tel_fijo',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='rubro',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Rubro'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Telefono de Contacto'),
        ),
        migrations.AlterField(
            model_name='autoridad',
            name='celular',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='autoridad',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='autoridad',
            name='tel_fijo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono Fijo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='celular',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tel_fijo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono Fijo'),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='celular',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='tel_fijo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono Fijo'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='domicilio',
            field=models.CharField(max_length=100, verbose_name='Domicilio'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=models.CharField(max_length=120, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='actividad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Actividad'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='celular',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='saldo',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Al dia / Debe'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='tel_fijo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono Fijo'),
        ),
    ]

# Generated by Django 2.2 on 2019-12-04 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0016_auto_20191128_1351'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfesionalXConsultorios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(blank=True, null=True, verbose_name='Dia')),
                ('hora_inicio', models.DateTimeField(blank=True, null=True, verbose_name='Hora Inicio')),
                ('hora_fin', models.DateTimeField(blank=True, null=True, verbose_name='Hora Fin')),
            ],
        ),
        migrations.CreateModel(
            name='RutinaXEjercicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True, verbose_name='Peso')),
                ('repeticiones', models.IntegerField(blank=True, null=True, verbose_name='Repeticiones')),
                ('series', models.IntegerField(blank=True, null=True, verbose_name='Repeticiones')),
            ],
        ),
        migrations.DeleteModel(
            name='PagoAProveedores',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='horarios',
        ),
        migrations.RemoveField(
            model_name='caja',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='consultorio',
            name='duracion_contrato',
        ),
        migrations.RemoveField(
            model_name='consultorio',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='consultorio',
            name='profesional',
        ),
        migrations.RemoveField(
            model_name='cuota',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='cuota',
            name='metodo',
        ),
        migrations.RemoveField(
            model_name='rutina',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='turno',
            name='fecha',
        ),
        migrations.AddField(
            model_name='asistenciaempleado',
            name='tipo',
            field=models.BooleanField(blank=True, choices=[('E', 'Entrada'), ('S', 'Salida')], null=True),
        ),
        migrations.AddField(
            model_name='asistenciasocio',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Sucursal'),
        ),
        migrations.AddField(
            model_name='autoridad',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Inicio'),
        ),
        migrations.AddField(
            model_name='autoridad',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Perfil'),
        ),
        migrations.AddField(
            model_name='autoridad',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Sucursal'),
        ),
        migrations.AddField(
            model_name='caja',
            name='metodo_pago',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Metodo de Pago'),
        ),
        migrations.AddField(
            model_name='caja',
            name='motivo',
            field=models.CharField(blank=True, choices=[('Pago', 'Pago a Proveedores'), ('Cobro', 'Cobro Cuota')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='consultorio',
            name='fecha_apertura',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Apertura'),
        ),
        migrations.AddField(
            model_name='cuota',
            name='fecha_vencimiento',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha del Vencimiento'),
        ),
        migrations.AddField(
            model_name='ejercicio',
            name='musculo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Musculo'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='ficha_medica',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Ficha Medica'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Perfil'),
        ),
        migrations.AddField(
            model_name='horario',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Empleado'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='codigo_insumo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Codigo del Insumo'),
        ),
        migrations.AddField(
            model_name='insumo',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Proveedor'),
        ),
        migrations.AddField(
            model_name='liquidacion',
            name='cantidad_horas',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de Horas Liquidadas'),
        ),
        migrations.AddField(
            model_name='liquidacion',
            name='empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Empleado'),
        ),
        migrations.AddField(
            model_name='liquidacion',
            name='monto_total',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=10, null=True, verbose_name='Total Liquidado'),
        ),
        migrations.AddField(
            model_name='liquidacion',
            name='precio_hora',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio Hora Liquidada'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='fecha_desde',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Desde'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='fecha_hasta',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha Hasta'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto de Perfil'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='saldo',
            field=models.DecimalField(blank=True, choices=[('Al dia', 'Al dia'), ('Debe', 'Debe')], decimal_places=10, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='rutina',
            name='cantidad_dias',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cantidad de Dias Semanales'),
        ),
        migrations.AddField(
            model_name='rutina',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripcion'),
        ),
        migrations.AddField(
            model_name='socio',
            name='actividades',
            field=models.ManyToManyField(blank=True, to='SmartGym.Actividad'),
        ),
        migrations.AddField(
            model_name='turno',
            name='horario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Horario'),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='estado',
            field=models.IntegerField(blank=True, choices=[('B', 'Bueno'), ('M', 'Malo'), ('R', 'En Reparacion')], null=True),
        ),
        migrations.AlterField(
            model_name='liquidacion',
            name='fecha',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de la liquidacion'),
        ),
        migrations.AlterField(
            model_name='profesional',
            name='profesion',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Profesion'),
        ),
        migrations.RemoveField(
            model_name='rutina',
            name='ejercicio',
        ),
        migrations.AddField(
            model_name='rutinaxejercicio',
            name='ejercicio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Ejercicio'),
        ),
        migrations.AddField(
            model_name='rutinaxejercicio',
            name='rutina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Rutina'),
        ),
        migrations.AddField(
            model_name='profesionalxconsultorios',
            name='consultorio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Consultorio'),
        ),
        migrations.AddField(
            model_name='profesionalxconsultorios',
            name='profesional',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Profesional'),
        ),
        migrations.AddField(
            model_name='profesional',
            name='consultorios',
            field=models.ManyToManyField(blank=True, through='SmartGym.ProfesionalXConsultorios', to='SmartGym.Consultorio'),
        ),
        migrations.AddField(
            model_name='rutina',
            name='ejercicio',
            field=models.ManyToManyField(blank=True, through='SmartGym.RutinaXEjercicio', to='SmartGym.Ejercicio'),
        ),
    ]

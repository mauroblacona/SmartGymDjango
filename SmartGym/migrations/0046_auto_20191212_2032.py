# Generated by Django 2.2 on 2019-12-12 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0045_auto_20191212_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caja',
            name='metodo_pago',
        ),
        migrations.AddField(
            model_name='caja',
            name='cuota',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SmartGym.Cuota'),
        ),
        migrations.AddField(
            model_name='cuota',
            name='codigo_transaccion',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Codigo de la transaccion'),
        ),
        migrations.AddField(
            model_name='cuota',
            name='metodo_pago',
            field=models.CharField(blank=True, choices=[('Efectivo', 'Efectivo'), ('Debito', 'Debito'), ('Credito', 'Credito'), ('Otro', 'Otro')], max_length=50, null=True, verbose_name='Metodo de Pago'),
        ),
    ]
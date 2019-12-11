# Generated by Django 2.2 on 2019-12-10 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0029_auto_20191210_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liquidacion',
            name='monto_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Total Liquidado'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='monto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Monto'),
        ),
    ]

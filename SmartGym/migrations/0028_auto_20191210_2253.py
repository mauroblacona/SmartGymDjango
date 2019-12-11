# Generated by Django 2.2 on 2019-12-10 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0027_auto_20191210_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='monto',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, verbose_name='Monto'),
        ),
        migrations.AlterField(
            model_name='liquidacion',
            name='monto_total',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, verbose_name='Total Liquidado'),
        ),
    ]

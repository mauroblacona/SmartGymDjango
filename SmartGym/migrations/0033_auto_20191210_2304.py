# Generated by Django 2.2 on 2019-12-10 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0032_auto_20191210_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='saldo',
            field=models.CharField(blank=True, choices=[('Al dia', 'Al dia'), ('Deuda', 'Deuda'), ('Indefinido', 'Indefinido')], max_length=150, null=True),
        ),
    ]

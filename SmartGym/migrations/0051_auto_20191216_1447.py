# Generated by Django 2.2 on 2019-12-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0050_auto_20191216_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='cuenta',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cuenta'),
        ),
    ]
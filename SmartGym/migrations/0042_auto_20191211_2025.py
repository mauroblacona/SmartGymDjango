# Generated by Django 2.2 on 2019-12-11 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartGym', '0041_auto_20191211_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='status',
            field=models.CharField(blank=True, choices=[('AC', 'Activo'), ('IN', 'Inactivo')], max_length=150, null=True),
        ),
    ]

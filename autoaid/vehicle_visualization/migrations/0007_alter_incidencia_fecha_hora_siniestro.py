# Generated by Django 4.2.5 on 2024-03-18 18:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_visualization', '0006_alter_incidencia_fecha_hora_siniestro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencia',
            name='fecha_hora_siniestro',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Fecha y hora del siniestro'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.5 on 2024-03-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_visualization', '0007_alter_incidencia_fecha_hora_siniestro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencia',
            name='fecha_hora_siniestro',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora del siniestro'),
        ),
    ]

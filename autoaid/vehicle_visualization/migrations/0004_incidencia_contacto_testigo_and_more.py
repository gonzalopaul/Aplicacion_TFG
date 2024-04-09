# Generated by Django 4.2.5 on 2024-03-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_visualization', '0003_incidencia_imagen_atras_incidencia_imagen_capo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidencia',
            name='contacto_testigo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Contacto del testigo'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='fecha_hora_siniestro',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha y hora del siniestro'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='llamada_policia',
            field=models.BooleanField(default=False, verbose_name='¿Se llamó a la policía?'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='marca_modelo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca y Modelo'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='matricula',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Matrícula'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='nombre_asegurado',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre y Apellidos del asegurado'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='numero_incidencia_policial',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Número de incidencia policial'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='telefono_movil',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono móvil'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='testigo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Testigo'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='tipo_aparcamiento',
            field=models.BooleanField(blank=True, null=True, verbose_name='Tipo de Aparcamiento'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='ubicacion_siniestro',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ubicación del siniestro'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='vehiculos_propiedades_involucrados',
            field=models.TextField(blank=True, null=True, verbose_name='Vehículos o propiedades involucrados'),
        ),
    ]
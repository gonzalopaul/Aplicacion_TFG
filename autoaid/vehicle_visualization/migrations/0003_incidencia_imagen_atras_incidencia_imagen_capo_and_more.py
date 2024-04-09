# Generated by Django 4.2.5 on 2024-02-21 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_visualization', '0002_alter_incidencia_nivel_dano_atras_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidencia',
            name='imagen_atras',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_incidencias/atras/'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='imagen_capo',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_incidencias/capo/'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='imagen_lateral_der',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_incidencias/lateral_der/'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='imagen_lateral_izq',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_incidencias/lateral_izq/'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='imagen_paragolpes',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_incidencias/paragolpes/'),
        ),
        migrations.AddField(
            model_name='incidencia',
            name='imagen_techo',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_incidencias/techo/'),
        ),
    ]
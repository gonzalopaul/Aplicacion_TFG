# Generated by Django 4.2.5 on 2024-02-19 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0008_remove_customuser_numero_de_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=14),
        ),
    ]

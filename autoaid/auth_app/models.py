from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('usuario', 'Usuario'),
        ('admin', 'Admin'),
        ('user', 'User'),  # Añadido
        ('worker', 'Worker'),  # Añadido
    )
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=False, max_length=14)
    rol = models.CharField(max_length=10, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'  # Utiliza el email como identificador principal
    REQUIRED_FIELDS = ['username', 'nombre', 'apellidos']  # Campos requeridos además del email y password


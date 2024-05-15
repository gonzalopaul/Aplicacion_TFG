from django.db import models
from django.conf import settings

# Create your models here.
TIPO_APARCAMIENTO_CHOICES = (
    ('si', 'Sí'),
    ('no', 'No'),
)
ESTADO_CHOICES = (
    ('pendiente', 'Pendiente'),
    ('en_revision', 'En revisión'),
    ('cerrado', 'Cerrado'),
)
ESTADOS_INVESTIGACION = [
    ('pendiente', 'Pendiente'),
    ('en_progreso', 'En Progreso'),
    ('datos_insuficientes', 'Datos Insuficientes'),
    ('en_espera_de_documentacion', 'En Espera de Documentación'),
    ('fraude_confirmado', 'Fraude Confirmado'),
    ('sin_fraude', 'Sin Fraude'),
    ('fraude_sospechoso', 'Fraude Sospechoso'),
    ('archivado', 'Archivado'),
    ('revision_externa', 'Revisión Externa'),
    ('en_litigio', 'En Litigio'),
]
class Incidencia(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, verbose_name='email', null=True)
    descripcion = models.TextField()
    nivel_dano_capo = models.IntegerField(choices=[(i, i) for i in range(0, 5)])
    imagen_capo = models.ImageField(upload_to='imagenes_incidencias/capo/', blank=True, null=True)
    nivel_dano_paragolpes = models.IntegerField(choices=[(i, i) for i in range(0, 5)])
    imagen_paragolpes = models.ImageField(upload_to='imagenes_incidencias/paragolpes/', blank=True, null=True)
    nivel_dano_lateral_izq = models.IntegerField(choices=[(i, i) for i in range(0, 5)])
    imagen_lateral_izq = models.ImageField(upload_to='imagenes_incidencias/lateral_izq/', blank=True, null=True)
    nivel_dano_lateral_der = models.IntegerField(choices=[(i, i) for i in range(0, 5)])
    imagen_lateral_der = models.ImageField(upload_to='imagenes_incidencias/lateral_der/', blank=True, null=True)
    nivel_dano_techo = models.IntegerField(choices=[(i, i) for i in range(0, 5)])
    imagen_techo = models.ImageField(upload_to='imagenes_incidencias/techo/', blank=True, null=True)
    nivel_dano_atras = models.IntegerField(choices=[(i, i) for i in range(0, 5)])
    imagen_atras = models.ImageField(upload_to='imagenes_incidencias/atras/', blank=True, null=True)

    fecha_hora_siniestro = models.DateTimeField(verbose_name='Fecha y hora del siniestro', null=True)
    ubicacion_siniestro = models.CharField(max_length=255, verbose_name='Ubicación del siniestro', null=True)

    tipo_aparcamiento = models.CharField(
        max_length=2,
        choices=TIPO_APARCAMIENTO_CHOICES,
        verbose_name='Tipo de Aparcamiento',
        default="no"
    )
    matricula = models.CharField(max_length=20, verbose_name='Matrícula', null=True)
    marca_modelo = models.CharField(max_length=50, verbose_name='Marca y Modelo', null=True)
    nombre_asegurado = models.CharField(max_length=100, verbose_name='Nombre y Apellidos del asegurado', null=True)
    telefono_movil = models.CharField(max_length=20, verbose_name='Teléfono móvil', null=True)
    vehiculos_propiedades_involucrados = models.TextField(verbose_name='Vehículos o propiedades involucrados', null=True, blank=True)
    testigo = models.CharField(max_length=100, verbose_name='Testigo', null=True, blank=True)
    contacto_testigo = models.CharField(max_length=100, verbose_name='Contacto del testigo', null=True, blank=True)

    llamada_policia = models.CharField(
        max_length=2,
        choices=TIPO_APARCAMIENTO_CHOICES,
        verbose_name='¿Se llamó a la policía?',
        default="no"
    )
    numero_incidencia_policial = models.CharField(max_length=50, verbose_name='Número de incidencia policial', null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='pendiente',
        verbose_name='Estado'
    )

class HistorialIncidencia(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, verbose_name='email', null=True)
    descripcion = models.TextField()
    fecha_hora_siniestro = models.DateTimeField(verbose_name='Fecha y hora del siniestro', null=True)
    ubicacion_siniestro = models.CharField(max_length=255, verbose_name='Ubicación del siniestro', null=True)

    tipo_aparcamiento = models.CharField(
        max_length=2,
        choices=TIPO_APARCAMIENTO_CHOICES,
        verbose_name='Tipo de Aparcamiento',
        default="no"
    )
    matricula = models.CharField(max_length=20, verbose_name='Matrícula', null=True)
    marca_modelo = models.CharField(max_length=50, verbose_name='Marca y Modelo', null=True)
    nombre_asegurado = models.CharField(max_length=100, verbose_name='Nombre y Apellidos del asegurado', null=True)
    telefono_movil = models.CharField(max_length=20, verbose_name='Teléfono móvil', null=True)
    vehiculos_propiedades_involucrados = models.TextField(verbose_name='Vehículos o propiedades involucrados', null=True, blank=True)
    testigo = models.CharField(max_length=100, verbose_name='Testigo', null=True, blank=True)
    contacto_testigo = models.CharField(max_length=100, verbose_name='Contacto del testigo', null=True, blank=True)

class Poliza(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    tipo_poliza = models.CharField(max_length=50, verbose_name="Tipo de Póliza")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio")
    fecha_fin = models.DateField(verbose_name="Fecha de Fin")
    condiciones = models.TextField(verbose_name="Condiciones de la Póliza", blank=True, null=True)
    edad_conductor = models.IntegerField(verbose_name="Edad del Conductor", default=0)
    anos_carnet = models.IntegerField(verbose_name="Años de Carnet", default=0)
    puntos_carnet = models.IntegerField(verbose_name="Puntos del Carnet", default=0)
    importe_poliza = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Importe de la Póliza", default=0)


    def __str__(self):
        return f"{self.tipo_poliza} - {self.usuario.email}"

class HistorialFraudes(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Usuario")
    fecha_incidente = models.DateField(verbose_name="Fecha del Incidente", blank=True, null= True)
    descripcion = models.TextField(verbose_name="Descripción del Fraude", blank=True, null=True)
    estado_investigacion = models.CharField(
    max_length=50,
    choices=ESTADOS_INVESTIGACION,
    default='pendiente',
    verbose_name="Estado de la Investigación"
)

    def __str__(self):
        return f"Fraude - {self.fecha_incidente} - {self.usuario.email}"

class IncidenciaRevisada(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    incidencia_id = models.IntegerField()  # Asume que incidencia_id es un entero
    respuestas_json = models.TextField()  # Para almacenar el JSON de respuestas
    recomendaciones_json = models.TextField()  # Para almacenar el JSON de recomendaciones
    # Puedes añadir cualquier otro campo que necesites

    def __str__(self):
        return f"Incidencia revisada para el usuario {self.usuario.username} - Incidencia ID {self.incidencia_id}"
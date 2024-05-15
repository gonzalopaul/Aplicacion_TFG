import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from vehicle_visualization.models import Incidencia, Poliza, HistorialFraudes

User = get_user_model()

@pytest.mark.django_db
class IncidenciaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.incidencia = Incidencia.objects.create(
            usuario=self.user,
            email='testuser@example.com',
            descripcion='Descripción de prueba',
            nivel_dano_capo=2,
            nivel_dano_paragolpes=3,
            nivel_dano_lateral_izq=1,
            nivel_dano_lateral_der=4,
            nivel_dano_techo=0,
            nivel_dano_atras=2,
            fecha_hora_siniestro='2023-01-01 10:00:00',
            ubicacion_siniestro='Ubicación de prueba',
            tipo_aparcamiento='si',
            matricula='ABC123',
            marca_modelo='Marca y Modelo de Prueba',
            nombre_asegurado='Nombre Asegurado',
            telefono_movil='123456789',
            vehiculos_propiedades_involucrados='Otro vehículo involucrado',
            testigo='Nombre Testigo',
            contacto_testigo='123456789',
            llamada_policia='no',
            numero_incidencia_policial='',
            estado='pendiente'
        )

    def test_incidencia_creation(self):
        self.assertEqual(self.incidencia.usuario.username, 'testuser')
        self.assertEqual(self.incidencia.email, 'testuser@example.com')
        self.assertEqual(self.incidencia.descripcion, 'Descripción de prueba')

@pytest.mark.django_db
class PolizaModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser2', password='12345')
        self.poliza = Poliza.objects.create(
            usuario=self.user,
            tipo_poliza='Comprehensive',
            fecha_inicio='2023-01-01',
            fecha_fin='2024-01-01',
            condiciones='Condiciones de la póliza',
            edad_conductor=30,
            anos_carnet=10,
            puntos_carnet=12,
            importe_poliza=500.00
        )

    def test_poliza_creation(self):
        self.assertEqual(self.poliza.usuario.username, 'testuser2')
        self.assertEqual(self.poliza.tipo_poliza, 'Comprehensive')
        self.assertEqual(self.poliza.importe_poliza, 500.00)

@pytest.mark.django_db
class HistorialFraudesModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser3', password='12345')
        self.fraude = HistorialFraudes.objects.create(
            usuario=self.user,
            fecha_incidente='2023-01-01',
            descripcion='Descripción del fraude',
            estado_investigacion='pendiente'
        )

    def test_fraude_creation(self):
        self.assertEqual(self.fraude.usuario.username, 'testuser3')
        self.assertEqual(self.fraude.descripcion, 'Descripción del fraude')
        self.assertEqual(self.fraude.estado_investigacion, 'pendiente')

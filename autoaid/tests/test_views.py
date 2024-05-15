import pytest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from vehicle_visualization.models import Incidencia

User = get_user_model()

@pytest.mark.django_db
class ViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_car_view(self):
        response = self.client.get(reverse('car_view'))
        self.assertEqual(response.status_code, 200)

    def test_detalle_incidencia_view(self):
        incidencia = Incidencia.objects.create(
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
        response = self.client.get(reverse('detalle_incidencia', args=[incidencia.pk]))
        self.assertEqual(response.status_code, 200)

    def test_eliminar_incidencia_view(self):
        incidencia = Incidencia.objects.create(
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
        response = self.client.get(reverse('eliminar_incidencia', args=[incidencia.pk]))
        self.assertEqual(response.status_code, 302)  # Redirect after delete

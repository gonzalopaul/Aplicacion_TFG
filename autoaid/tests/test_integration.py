from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from vehicle_visualization.models import Incidencia, Poliza, HistorialFraudes, IncidenciaRevisada

User = get_user_model()

class DroolsIntegrationTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='12345')
        self.client.login(username='testuser', password='12345')
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

    def test_enviar_datos_drools(self):
        datos_incidencia = {
            "ubicacion": self.incidencia.ubicacion_siniestro,
            "fechaYHora": self.incidencia.fecha_hora_siniestro.strftime('%Y-%m-%dT%H:%M:%S'),
            "tipoAparcamiento": self.incidencia.tipo_aparcamiento,
            "llamadaPolicia": self.incidencia.llamada_policia,
            "matricula": self.incidencia.matricula,
            "numeroIncidenciaPolicial": self.incidencia.numero_incidencia_policial,
            "testigo": self.incidencia.testigo,
            "contactoTestigo": self.incidencia.contacto_testigo,
            "vehiculosPropiedadesInvolucrados": self.incidencia.vehiculos_propiedades_involucrados,
            "reincidenciaUltimoAnno": 0,
            "reincidencia3Anno": 0,
            "fraudes": 0,
            "tipoCobertura": self.poliza.tipo_poliza,
            "inicioPoliza": self.poliza.fecha_inicio.strftime('%Y-%m-%d'),
            "finPoliza": self.poliza.fecha_fin.strftime('%Y-%m-%d'),
            "edadConductor": self.poliza.edad_conductor,
            "anosCarnet": self.poliza.anos_carnet,
            "importePoliza": self.poliza.importe_poliza,
            "puntosCarnet": self.poliza.puntos_carnet
        }

        response = self.client.post('http://localhost:8080/procesar-siniestro', json=datos_incidencia)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('respuestas', data)
        self.assertIn('recomendaciones', data)

        respuestas_recomendaciones = {
            "incidencia_id": self.incidencia.id,
            "respuestas": data['respuestas'],
            "recomendaciones": data['recomendaciones']
        }

        response_django = self.client.post('/procesar-respuesta-drools/', json=respuestas_recomendaciones, content_type='application/json')
        self.assertEqual(response_django.status_code, 200)
        self.assertTrue(IncidenciaRevisada.objects.filter(incidencia_id=self.incidencia.id).exists())

from locust import HttpUser, TaskSet, task

class UserBehavior(TaskSet):

    def on_start(self):
        self.login()

    def login(self):
        self.client.post("/login/", {
            "username": "testuser",
            "password": "12345"
        })

    @task
    def create_incidencia(self):
        self.client.post("/incidencias/create/", {
            'email': 'testuser@example.com',
            'descripcion': 'Descripción de prueba',
            'nivel_dano_capo': 2,
            'nivel_dano_paragolpes': 3,
            'nivel_dano_lateral_izq': 1,
            'nivel_dano_lateral_der': 4,
            'nivel_dano_techo': 0,
            'nivel_dano_atras': 2,
            'fecha_hora_siniestro': '2023-01-01 10:00:00',
            'ubicacion_siniestro': 'Ubicación de prueba',
            'tipo_aparcamiento': 'si',
            'matricula': 'ABC123',
            'marca_modelo': 'Marca y Modelo de Prueba',
            'nombre_asegurado': 'Nombre Asegurado',
            'telefono_movil': '123456789',
            'vehiculos_propiedades_involucrados': 'Otro vehículo involucrado',
            'testigo': 'Nombre Testigo',
            'contacto_testigo': '123456789',
            'llamada_policia': 'no',
            'numero_incidencia_policial': '',
            'estado': 'pendiente'
        })

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000

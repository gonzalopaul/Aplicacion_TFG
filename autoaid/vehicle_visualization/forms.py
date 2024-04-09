from django import forms
from .models import Incidencia, ESTADO_CHOICES

ESTADO_CHOICES_CON_TODOS = [('', 'Todos')] + list(ESTADO_CHOICES)

class IncidenciaForm(forms.ModelForm):

    class Meta:
        model = Incidencia
        fields = ['nivel_dano_capo', 
                'descripcion', 
                'nivel_dano_paragolpes', 
                'nivel_dano_lateral_izq', 
                'nivel_dano_lateral_der', 
                'nivel_dano_techo', 
                'nivel_dano_atras',

                'fecha_hora_siniestro',
                'ubicacion_siniestro',
                'tipo_aparcamiento',
                'matricula',
                'marca_modelo',
                'nombre_asegurado',
                'telefono_movil',
                'vehiculos_propiedades_involucrados',
                'testigo',
                'contacto_testigo',
                'llamada_policia',
                'numero_incidencia_policial',
                  ]
        widgets = {
            'fecha_hora_siniestro': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'tipo_aparcamiento': forms.Select(),
            'llamada_policia': forms.Select(),
        }

class FiltroIncidenciasForm(forms.Form):
    descripcion = forms.CharField(required=False, label='Descripción')
    fecha_hora_siniestro = forms.DateTimeField(required=False, label='Fecha y hora del siniestro')
    matricula = forms.CharField(required=False, label='Matrícula')
    marca_modelo = forms.CharField(required=False, label='Marca y Modelo')
    estado = forms.ChoiceField(choices=ESTADO_CHOICES_CON_TODOS, required=False, label='Estado')
     # Puedes agregar tantos campos de filtro como necesites

class CambiarEstadoIncidenciaForm(forms.ModelForm):
    # Define las opciones permitidas para el estado
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_revision', 'En revisión'),
        ('cerrado', 'Cerrado'),
    ]

    # Usa ChoiceField para el campo estado
    estado = forms.ChoiceField(choices=ESTADO_CHOICES, label="Nuevo Estado")

    class Meta:
        model = Incidencia
        fields = ['estado']
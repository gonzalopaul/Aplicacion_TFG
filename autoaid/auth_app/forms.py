from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from vehicle_visualization.models import Poliza
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['nombre', 'apellidos', 'email']

class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['nombre', 'apellidos', 'email']

class CustomUserForm(forms.Form):
    user = forms.ModelChoiceField(
        queryset=CustomUser.objects.all(),
        label="Usuario",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label=None
    )
    rol = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        label="Rol",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class UsuarioFiltroForm(forms.Form):
    usuario = forms.ModelChoiceField(
        queryset=CustomUser.objects.all().order_by('email'),
        label="Seleccione un usuario",
        empty_label="Seleccione un usuario",
        required=False
    )

class HistorialIncidenciasCSVForm(forms.Form):
    incidencias_csv = forms.FileField(label='Cargar CSV de Incidencias', help_text='Archivo CSV', widget=forms.FileInput(attrs={'accept': '.csv'}))

class HistorialFraudesCSVForm(forms.Form):
    fraudes_csv = forms.FileField(label='Cargar CSV de Fraudes', help_text='Archivo CSV', widget=forms.FileInput(attrs={'accept': '.csv'}))

class PolizaForm(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = ['tipo_poliza', 'fecha_inicio', 'fecha_fin', 'condiciones', 'edad_conductor', 'anos_carnet', 'puntos_carnet', 'importe_poliza']

    def __init__(self, *args, **kwargs):
        super(PolizaForm, self).__init__(*args, **kwargs)
        # Puedes añadir personalizaciones adicionales aquí si es necesario
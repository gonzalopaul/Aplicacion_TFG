from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
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
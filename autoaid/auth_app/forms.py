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
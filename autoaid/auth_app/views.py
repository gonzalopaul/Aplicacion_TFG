from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm  # Este es el formulario de login predeterminado de Django
from .forms import *  # Asegúrate de tener este formulario definido en forms.py
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import CustomUser
from vehicle_visualization.models import *
import csv
from datetime import date, timedelta
from django.contrib import messages

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirige a la página principal tras el login exitoso
#         else:
#             # Manejar aquí el caso de formulario no válido
#             pass
#     else:
#         form = AuthenticationForm()
#     return render(request, 'auth_app/login.html', {'form': form})

# def register_view(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Logea al usuario directamente tras el registro
#             return redirect('home')  # Redirige a la página principal
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'auth_app/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la página de login tras el logout

def home_view(request):
    # Asegúrate de que el usuario está autenticado para ver esta página
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'auth_app/home.html')

def login_and_register_view(request):
    if request.method == 'POST':
        if 'login' in request.POST: 
            login_form = AuthenticationForm(request, data=request.POST)
            register_form = CustomUserCreationForm()
            if login_form.is_valid():
                user = authenticate(username=login_form.cleaned_data['username'],
                                    password=login_form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('home')  
        elif 'register' in request.POST: 
            login_form = AuthenticationForm()
            register_form = CustomUserCreationForm(request.POST)
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)  
                return redirect('home') 
    else:
        login_form = AuthenticationForm()
        register_form = CustomUserCreationForm()

    return render(request, 'auth_app/login.html', {
        'login_form': login_form,
        'register_form': register_form
    })

@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            rol = form.cleaned_data['rol']
            # Asegúrate de que el objeto 'user' es una instancia de CustomUser
            user.rol = rol
            user.save()
            return redirect('home')
    else:
        form = CustomUserForm()

    # Agregar la recuperación de todos los usuarios para mostrarlos en la tabla
    users = CustomUser.objects.all()

    # Pasar tanto el formulario como la lista de usuarios al contexto de la plantilla
    return render(request, 'auth_app/manage_users.html', {
        'form': form,
        'users': users
    })

@user_passes_test(lambda u: u.is_superuser or u.rol == "worker")
def historial_usuario(request):
    usuario_form = UsuarioFiltroForm(request.GET or None)
    incidencias_form = HistorialIncidenciasCSVForm()
    fraudes_form = HistorialFraudesCSVForm()

    historial_incidencias = HistorialIncidencia.objects.none()
    historial_fraudes = HistorialFraudes.objects.none()

    if request.method == 'POST':
        if 'submit_incidencias' in request.POST:
            incidencias_form = HistorialIncidenciasCSVForm(request.POST, request.FILES)
            if incidencias_form.is_valid() and usuario_form.is_valid():
                usuario = usuario_form.cleaned_data['usuario']
                handle_csv_incidencias(request.FILES['incidencias_csv'], usuario)
        elif 'submit_fraudes' in request.POST:
            fraudes_form = HistorialFraudesCSVForm(request.POST, request.FILES)
            if fraudes_form.is_valid() and usuario_form.is_valid():
                usuario = usuario_form.cleaned_data['usuario']
                handle_csv_fraudes(request.FILES['fraudes_csv'], usuario)
    else:
        if usuario_form.is_valid():
            usuario = usuario_form.cleaned_data.get('usuario')
            if usuario:
                historial_incidencias = HistorialIncidencia.objects.filter(usuario=usuario)
                historial_fraudes = HistorialFraudes.objects.filter(usuario=usuario)

    return render(request, 'auth_app/historial_usuario.html', {
        'usuario_form': usuario_form,
        'incidencias_form': incidencias_form,
        'fraudes_form': fraudes_form,
        'historial_incidencias': historial_incidencias,
        'historial_fraudes': historial_fraudes
    })


def handle_csv_fraudes(csv_file, usuario):
    # Verifica la decodificación correcta del archivo y elimina BOM si es necesario
    decoded_file = csv_file.read().decode('utf-8-sig').splitlines()
    reader = csv.DictReader(decoded_file)
    fraudes = []
    for row in reader:
        # Limpia las claves de cualquier espacio en blanco sobrante o caracteres extraños
        cleaned_row = {key.strip(): value for key, value in row.items()}
        # Asigna el usuario_id del usuario seleccionado a cada fila
        cleaned_row['usuario_id'] = usuario.id
        # Establece valores por defecto para campos que puedan faltar
        cleaned_row.setdefault('fecha_incidente', None)
        cleaned_row.setdefault('descripcion', '')
        cleaned_row.setdefault('estado_investigacion', 'pendiente')
        fraudes.append(HistorialFraudes(**cleaned_row))
    HistorialFraudes.objects.bulk_create(fraudes)

def handle_csv_incidencias(csv_file, usuario):
    # Verifica la decodificación correcta del archivo y elimina BOM si es necesario
    decoded_file = csv_file.read().decode('utf-8-sig').splitlines()
    reader = csv.DictReader(decoded_file)
    incidencias = []
    for row in reader:
        # Limpia las claves de cualquier espacio en blanco sobrante o caracteres extraños
        cleaned_row = {key.strip(): value for key, value in row.items()}
        # Asigna el usuario_id del usuario seleccionado a cada fila
        cleaned_row['usuario_id'] = usuario.id
        # Establece valores por defecto para campos que puedan faltar
        cleaned_row.setdefault('email', None)
        cleaned_row.setdefault('fecha_hora_siniestro', None)
        cleaned_row.setdefault('ubicacion_siniestro', None)
        cleaned_row.setdefault('tipo_aparcamiento', None)
        cleaned_row.setdefault('matricula', None)
        cleaned_row.setdefault('marca_modelo', None)
        cleaned_row.setdefault('nombre_asegurado', None)
        cleaned_row.setdefault('telefono_movil', None)
        cleaned_row.setdefault('vehiculos_propiedades_involucrados', None)
        cleaned_row.setdefault('testigo', None)
        cleaned_row.setdefault('contacto_testigo', None)
        cleaned_row.setdefault('descripcion', '')
        incidencias.append(HistorialIncidencia(**cleaned_row))
    HistorialIncidencia.objects.bulk_create(incidencias)

@user_passes_test(lambda u: u.is_superuser or u.rol == "worker")
def gestion_poliza(request):
    usuario_form = UsuarioFiltroForm(request.GET or None)
    poliza_form = None
    usuario = None

    # Recuperar el usuario desde el formulario o la URL
    if 'usuario' in request.GET and usuario_form.is_valid():
        usuario = usuario_form.cleaned_data['usuario']
        poliza, created = Poliza.objects.get_or_create(
            usuario=usuario,
            defaults={
                'fecha_inicio': date.today(),
                'fecha_fin': date.today() + timedelta(days=365),
                'tipo_poliza': "Básica",
                'condiciones': "Condiciones predeterminadas",
                'edad_conductor': 25,
                'anos_carnet': 5,
                'puntos_carnet': 12,
                'importe_poliza': 100.00
            }
        )
        poliza_form = PolizaForm(instance=poliza)

    # Procesar POST para actualizar o crear póliza
    if request.method == 'POST':
        if usuario:
            poliza = Poliza.objects.get(usuario=usuario)  # Asegúrate de que esta línea no falla
            poliza_form = PolizaForm(request.POST, instance=poliza)
            if poliza_form.is_valid():
                poliza_form.save()
                return redirect('gestion_poliza')
        else:
            return redirect('gestion_poliza')  # Redirect si no hay usuario seleccionado o en caso de error

    return render(request, 'auth_app/gestion_poliza.html', {
        'usuario_form': usuario_form,
        'poliza_form': poliza_form
    })

@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página del perfil
    else:
        form = CustomUserEditForm(instance=request.user)
    return render(request, 'auth_app/edit_profile.html', {'form': form})

@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        user.delete()  # Elimina el usuario
        logout(request)  # Cierra la sesión del usuario
        messages.success(request, 'Su cuenta ha sido eliminada.')
        return redirect('login')  # Redirige a la página de inicio o a donde consideres adecuado
    return render(request, 'auth_app/confirm_delete.html')
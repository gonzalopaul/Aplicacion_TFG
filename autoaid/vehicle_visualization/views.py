from django.shortcuts import render, redirect, get_object_or_404
from .forms import IncidenciaForm, FiltroIncidenciasForm, CambiarEstadoIncidenciaForm
from django.contrib import messages
from auth_app.models import CustomUser
from .models import Incidencia, HistorialFraudes
from django.core.paginator import Paginator
from django.contrib.auth.decorators import user_passes_test, login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import IncidenciaRevisada
from django.utils.decorators import method_decorator
from django.views import View



# Create your views here.

def car_view(request):
    if request.method == 'POST':
        form = IncidenciaForm(request.POST, request.FILES)
        email = request.POST.get('email')  # Obtiene el email directamente del formulario
        try:
            user = CustomUser.objects.get(email=email)  # Busca el usuario por email
            if form.is_valid():
                # En este punto, el formulario es válido, pero necesitas crear manualmente el objeto Incidencia
                # ya que el formulario no incluye todos los campos necesarios (como el usuario)
                incidencia = Incidencia(
                    usuario=user,
                    email = email,
                    descripcion=form.cleaned_data.get('descripcion', ''),
                    nivel_dano_capo=form.cleaned_data.get('nivel_dano_capo', None),
                    imagen_capo=request.FILES.get('imagen_capo', None),
                    nivel_dano_paragolpes=form.cleaned_data.get('nivel_dano_paragolpes', None),
                    imagen_paragolpes=request.FILES.get('imagen_paragolpes', None),
                    nivel_dano_lateral_izq=form.cleaned_data.get('nivel_dano_lateral_izq', None),
                    imagen_lateral_izq=request.FILES.get('imagen_lateral_izq', None),
                    nivel_dano_lateral_der=form.cleaned_data.get('nivel_dano_lateral_der', None),
                    imagen_lateral_der=request.FILES.get('imagen_lateral_der', None),
                    nivel_dano_techo=form.cleaned_data.get('nivel_dano_techo', None),
                    imagen_techo=request.FILES.get('imagen_techo', None),
                    nivel_dano_atras=form.cleaned_data.get('nivel_dano_atras', None),
                    imagen_atras=request.FILES.get('imagen_atras', None),

                    fecha_hora_siniestro=form.cleaned_data.get('fecha_hora_siniestro', None),
                    ubicacion_siniestro=form.cleaned_data.get('ubicacion_siniestro', None),
                    tipo_aparcamiento=form.cleaned_data.get('tipo_aparcamiento', None),
                    matricula=form.cleaned_data.get('matricula', None),
                    marca_modelo=form.cleaned_data.get('marca_modelo', None),
                    nombre_asegurado=form.cleaned_data.get('nombre_asegurado', None),
                    telefono_movil=form.cleaned_data.get('telefono_movil', None),
                    vehiculos_propiedades_involucrados=form.cleaned_data.get('vehiculos_propiedades_involucrados', None),
                    testigo=form.cleaned_data.get('testigo', None),
                    contacto_testigo=form.cleaned_data.get('contacto_testigo', None),
                    llamada_policia=form.cleaned_data.get('llamada_policia', None),
                    numero_incidencia_policial=form.cleaned_data.get('numero_incidencia_policial', None),
                    
                )
                incidencia.save()
                messages.success(request, 'Incidencia creada correctamente.')
                return redirect('/home')
            else:
                messages.error(request, 'Hay errores en el formulario.')
        except CustomUser.DoesNotExist:
            messages.error(request, 'No existe un usuario con ese email.')
    else:
        form = IncidenciaForm()

    return render(request, 'vehicle_visualization/car.html', {'form': form})

def moto_view(request):
    return render(request, 'vehicle_visualization/moto.html')

def suv_view(request):
    return render(request, 'vehicle_visualization/suv.html')

def deportivo_view(request):
    return render(request, 'vehicle_visualization/deportivo.html')

def cuatrox4_view(request):
    return render(request, 'vehicle_visualization/4x4.html')

def ranchera_view(request):
    return render(request, 'vehicle_visualization/ranchera.html')

@user_passes_test(lambda u: u.rol == 'worker' or u.is_superuser)
def dashboard_incidencias(request):
    filtro_form = FiltroIncidenciasForm(request.GET or None)
    
    if filtro_form.is_valid():
        incidencias = Incidencia.objects.all()

        descripcion = filtro_form.cleaned_data.get('descripcion')
        if descripcion:
            incidencias = incidencias.filter(descripcion__icontains=descripcion)

        fecha_hora_siniestro = filtro_form.cleaned_data.get('fecha_hora_siniestro')
        if fecha_hora_siniestro:
            incidencias = incidencias.filter(fecha_hora_siniestro=fecha_hora_siniestro)

        matricula = filtro_form.cleaned_data.get('matricula')
        if matricula:
            incidencias = incidencias.filter(matricula__icontains=matricula)

        marca_modelo = filtro_form.cleaned_data.get('marca_modelo')
        if marca_modelo:
            incidencias = incidencias.filter(marca_modelo__icontains=marca_modelo)

        estado = filtro_form.cleaned_data.get('estado')
        if estado:
            incidencias = incidencias.filter(estado__icontains=estado)

        # ... implementa más filtros si los necesitas ...

    else:
        incidencias = Incidencia.objects.none()  # Si el formulario no es válido, no mostramos resultados

    paginator = Paginator(incidencias, 10)  # 10 incidencias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'filtro_form': filtro_form,
        'incidencias': page_obj
    }

    return render(request, 'vehicle_visualization/dashboard.html', context)

@user_passes_test(lambda u: u.rol == 'worker' or u.is_superuser)
def detalle_incidencia(request, pk):
    # Recuperar la incidencia por el ID primario 'pk'
    incidencia = get_object_or_404(Incidencia, pk=pk)
    # Calcular el número de entradas en HistorialFraudes para el usuario relacionado con la incidencia
    conteo_fraudes = HistorialFraudes.objects.filter(usuario=incidencia.usuario).count()

    # Pasar la incidencia y el conteo de fraudes al template
    context = {
        'incidencia': incidencia,
        'conteo_fraudes': conteo_fraudes,
    }
    
    # Aquí puedes añadir cualquier lógica adicional que necesites, por ejemplo:
    # - Verificar si el usuario tiene permiso para ver esta incidencia
    # - Realizar alguna operación basada en la incidencia

    # Pasar la incidencia al template
    return render(request, 'vehicle_visualization/detalle_incidencia.html', context)

@login_required  # Asegura que solo usuarios autenticados puedan acceder a esta vista
def mis_incidencias(request):
    filtro_form = FiltroIncidenciasForm(request.GET or None)

    # Aquí asumimos que el modelo Incidencia tiene una clave foránea llamada 'usuario'
    # que relaciona la incidencia con el modelo de usuario.
    # Filtramos las incidencias para obtener solo aquellas del usuario actual.
    incidencias = Incidencia.objects.filter(usuario=request.user)

    if filtro_form.is_valid():
        descripcion = filtro_form.cleaned_data.get('descripcion')
        if descripcion:
            incidencias = incidencias.filter(descripcion__icontains=descripcion)

        fecha_hora_siniestro = filtro_form.cleaned_data.get('fecha_hora_siniestro')
        if fecha_hora_siniestro:
            incidencias = incidencias.filter(fecha_hora_siniestro=fecha_hora_siniestro)

        matricula = filtro_form.cleaned_data.get('matricula')
        if matricula:
            incidencias = incidencias.filter(matricula__icontains=matricula)

        marca_modelo = filtro_form.cleaned_data.get('marca_modelo')
        if marca_modelo:
            incidencias = incidencias.filter(marca_modelo__icontains=marca_modelo)

        # ... implementa más filtros si los necesitas ...

    paginator = Paginator(incidencias, 10)  # 10 incidencias por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'filtro_form': filtro_form,
        'incidencias': page_obj
    }

    return render(request, 'vehicle_visualization/mis_incidencias.html', context)

@method_decorator(csrf_exempt, name='dispatch')
class ProcesarRespuestaDroolsView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            # Asegúrate de que los campos 'incidencia_id', 'respuestas' y 'recomendaciones' se envían desde el frontend
            incidencia_id = data['incidencia_id']
            respuestas_json = data['respuestas']
            recomendaciones_json = data['recomendaciones']

            # Aquí puedes procesar los datos de respuestas y recomendaciones
            # Por ejemplo, guardarlos en la base de datos
            incidencia_revisada = IncidenciaRevisada(
                usuario=request.user,
                incidencia_id=incidencia_id,
                respuestas_json=json.dumps(respuestas_json),
                recomendaciones_json=json.dumps(recomendaciones_json)
            )
            incidencia_revisada.save()

            # Envía una respuesta de vuelta al cliente
            return JsonResponse({"mensaje": "Respuestas y recomendaciones recibidas y guardadas correctamente."}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Formato de datos incorrecto"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
def ver_analisis_drools(request, incidencia_id):
    # Usa 'latest' para obtener la revisión más reciente por 'id'
    try:
        analisis = IncidenciaRevisada.objects.filter(incidencia_id=incidencia_id).latest('id')
    except IncidenciaRevisada.DoesNotExist:
        analisis = None

    incidencia = get_object_or_404(Incidencia, id=incidencia_id)
    form = CambiarEstadoIncidenciaForm(instance=incidencia)

    if request.method == 'POST':
        form = CambiarEstadoIncidenciaForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            return redirect('vehicle_visualization:ver_analisis_drools', incidencia_id=incidencia_id)
    
    # Inicializar variables en caso de que 'analisis' no exista
    respuestas, recomendaciones = [], []
    if analisis:
        respuestas = json.loads(analisis.respuestas_json)
        recomendaciones = json.loads(analisis.recomendaciones_json)
    
    return render(request, 'vehicle_visualization/analisis.html', {
        'respuestas': respuestas,
        'recomendaciones': recomendaciones,
        'incidencia_id': incidencia_id,
        'form': form
    })
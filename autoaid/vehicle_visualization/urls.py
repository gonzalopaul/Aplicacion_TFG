from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'vehicle_visualization'

urlpatterns = [
    path('car/', views.car_view, name='car_view'),
    path('moto/', views.moto_view, name='moto_view'),
    path('suv/', views.suv_view, name='suv_view'),
    path('ranchera/', views.ranchera_view, name='ranchera_view'),
    path('4x4/', views.cuatrox4_view, name='4x4_view'),
    path('deportivo/', views.deportivo_view, name='deportivo_view'),
    path('dashboard/', views.dashboard_incidencias, name='dashboard_incidencias'),
    path('incidencia/<int:pk>/', views.detalle_incidencia, name='detalle_incidencia'),
    path('mis-incidencias/', views.mis_incidencias, name='mis_incidencias'),
    path('procesar-respuesta-drools/', views.ProcesarRespuestaDroolsView.as_view(), name='procesar_respuesta_drools'),
    path('incidencia/<int:incidencia_id>/analisis/', views.ver_analisis_drools, name='ver_analisis_drools'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

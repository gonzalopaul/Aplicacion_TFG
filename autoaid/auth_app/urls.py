# auth_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_and_register_view, name='login_and_register'),
    path('login/', views.login_and_register_view, name='login'),
    path('login/', views.login_and_register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('historial-usuario/', views.historial_usuario, name='historial_usuario'),
    path('gestionar-poliza/', views.gestion_poliza, name='gestion_poliza'),
    path('edit_profile/', views.edit_user_profile, name='edit_profile'),
    path('delete_account/', views.delete_user, name='delete_account'),
]

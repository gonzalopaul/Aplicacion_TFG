from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm  # Este es el formulario de login predeterminado de Django
from .forms import CustomUserCreationForm, CustomUserForm  # Asegúrate de tener este formulario definido en forms.py
from django.contrib.auth.decorators import user_passes_test, login_required
from .models import CustomUser

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
            user.rol = rol
            user.save()
            return redirect('home')
    else:
        form = CustomUserForm()

    return render(request, 'auth_app/manage_users.html', {'form': form})
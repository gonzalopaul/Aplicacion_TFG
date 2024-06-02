
# TRABAJO FIN DE GRADO

[![logo2.png](https://i.postimg.cc/SRjL7BrZ/logo2.png)](https://postimg.cc/WqLJsfxr)

Aplicación para la gestión de siniestros de vehículos

 [EN] Vehicle Claims Management App

## Información del proyecto

Este proyecto consiste en una aplicación web para la gestión de siniestros de vehículos. Los usuarios pueden registrarse y, una vez validados por un administrador, reportar incidencias detalladas mediante un modelo 3D interactivo. La aplicación distingue entre roles de usuario (asegurado), trabajador de la aseguradora y administrador, ofreciendo funcionalidades específicas para cada uno. Los trabajadores pueden revisar, analizar y gestionar incidencias con el apoyo de Drools, un motor de reglas que automatiza el análisis y la detección de fraudes. Los administradores, además, pueden asignar roles y permisos a los usuarios. El despliegue se realiza mediante Docker, facilitando la instalación y ejecución de la aplicación. La integración con Drools se maneja a través de una API, permitiendo un análisis eficiente de los siniestros reportados.

## Información de despliegue
La aplicación está dockerizada. Por lo que tan sólo clonando el repositorio y construyendo el contenedor se podrá hacer uso de esta.
````
git clone https://github.com/gonzalopaul/Aplicacion_TFG.git
````
Dirígete al directorio principal:
````
cd Aplicacion_TFG
````
Arranca el contenedor:
````
docker-compose up --build
````

Dirígete a tu navegador y accede a la siguiente url:
````
http://127.0.0.1:8000/login
````

## Información de utilización

Para poder utilizar correctamente la aplicación se deberá de crear una cuenta. Esta cuenta carecerá de privilegios hasta que un administrador los conceda.

Hay una cuenta de administrador creada por defecto:

#### Admin
Email: admin@autoaid.com

Contraseña: Junio2001

Para más información consulte la documentación del proyecto. Puede encontrarla en la raíz del repositorio bajo el nombre de MemoriaTFG.pdf

## Authors and License

- [@gonzalopaul](https://www.github.com/gonzalopaul)


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)



# Gestión de Proyectos

Página web para la gestión de proyectos y asignación de tareas.

## Descripción

Este sistema de seguimiento de proyectos permite a los usuarios crear proyectos, asignar tareas, gestionar funciones y realizar un seguimiento del progreso de forma eficaz, escalable y segura.

## Características principales

- Creación y gestión de proyectos y tareas
- Asignación de roles y permisos a diferentes usuarios (gerente, desarrollador y cliente)
- API escalable para la gestión de proyectos y actualización de estado
- Sistema de autenticación y seguridad

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados:

- Python 3.12.6
- Git

### Instalación de Python 3.12.6

1. Visita la [página oficial de Python](https://www.python.org/downloads/).
2. Descarga la versión 3.12.6 para tu sistema operativo.
3. Ejecuta el instalador y sigue las instrucciones.
4. Verifica la instalación abriendo una terminal y escribiendo:
   ```
   python --version
   ```

### Instalación de Git

1. Visita la [página oficial de Git](https://git-scm.com/downloads).
2. Descarga la versión para tu sistema operativo.
3. Ejecuta el instalador y sigue las instrucciones.
4. Verifica la instalación abriendo una terminal y escribiendo:
   ```
   git --version
   ```

## Cómo instalar y ejecutar el proyecto

### Para Mac/Linux

1. Abre una terminal.
2. Clona el repositorio:
   ```
   git clone https://github.com/Santalexx/project-manager.git
   ```
3. Entra al directorio del proyecto:
   ```
   cd project-manager
   ```
4. Crea un entorno virtual:
   ```
   python3 -m venv venv
   ```
5. Activa el entorno virtual:
   ```
   source venv/bin/activate
   ```
6. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
7. Realiza las migraciones:
   ```
   python manage.py migrate
   ```
8. Crea un superusuario:
   ```
   python manage.py createsuperuser
   ```
9. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```
10. Abre un navegador y ve a `http://127.0.0.1:8000/`

### Para Windows

1. Abre Git Bash o el Símbolo del sistema.
2. Clona el repositorio:
   ```
   git clone https://github.com/Santalexx/project-manager.git
   ```
3. Entra al directorio del proyecto:
   ```
   cd project-manager
   ```
4. Crea un entorno virtual:
   ```
   python -m venv venv
   ```
5. Activa el entorno virtual:
   ```
   venv\Scripts\activate
   ```
6. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
7. Realiza las migraciones:
   ```
   python manage.py migrate
   ```
8. Crea un superusuario:
   ```
   python manage.py createsuperuser
   ```
9. Ejecuta el servidor de desarrollo:
   ```
   python manage.py runserver
   ```
10. Abre un navegador y ve a `http://127.0.0.1:8000/`


# Django Ejemplo
Basado en la guía de [Django Girls](https://tutorial.djangogirls.org/es/)

# Entorno virtual

[Instalación](https://tutorial.djangogirls.org/es/django_installation/)

```bash
mkdir django-ejemplo
cd django-ejemplo
```

Creación de un entorno virtual (requiere tener instalado *virtualenv*):

```bash
python3 -m venv env

source myvenv/bin/activate
```

Deberán ver algo como lo siguiente:

```bash
(env) ~/usuario$
```

¡Nota que el prefijo (env) aparece!

# Instalar Django

Requiere tener *pip* instalado:

```bash
# última versión
pip install django

# especificar versión
pip install django==1.8
```

Vamos a comprobar que se instaló Django correctmante obteniendo su versión:

```bash
python -m django --version
```

Ya tienes listo un entorno para trabajar con Django.

# Comenzar un proyecto

[Comenzar un proyecto en Django](https://tutorial.djangogirls.org/es/django_start_project/)

Tenemos disponible, dentro de nuestro entorno, herramientas de consola como
*django-admin*:

*django-admin.py* es un script que creará los archivos y directorios para ti.
Ahora deberías tener una estructura de directorios parecida a esto:

```bash
django-admin startproject misitio .
```

```
.
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   ├── pip-selfcheck.json
│   └── pyvenv.cfg
│   ...
├── manage.py
├── misitio
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── README.md

6 directories, 8 files
```

*manage.py* es un script que ayuda con la administración del sitio. Con ello
podremos iniciar un servidor web en nuestro ordenador sin necesidad de instalar
nada más, entre otras cosas.

El archivo *settings.py* contiene la configuración de tu sitio web.

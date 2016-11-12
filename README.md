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

# Configuración

Nuestro archivo de configuración se encuentra en *misitio/settings.py*.

Abrimos dicho archivo y vamos a configurar algunas cosas sencillas:

```python
# horario del sitio
TIME_ZONE = 'America/Argentina/Mendoza'

# archivos estáticos: CSS, Javascript, otros cargados por nuestra página
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Como base de datos usaremos la que viene por defecto, *SQLite3*. Nos va a
permitir guardar todos nuestros datos en un archivo que funcionará como base de
datos.

Una vez realizado esto, ya estamos listos para crear la base de datos. Nos
paramos sobre el directorio que contiene el script *manage.py* y ejecutamos:

```bash
python manage.py migrate
```

Deberíamos ver algo como lo siguiente:

```bash
Operations to perform:
  Apply all migrations: admin, contenttypes, auth, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK
```

¡Y listo! ¡Es hora de iniciar el servidor web y ver si nuestro sitio web está
funcionando!

# Iniciar servidor

```bash
python manage.py runserver
```

Y ya tendremos el servidor corriendo en nuestra PC:

```
http://127.0.0.1:8000/
```

> El servidor web se apropiará de tu consola hasta que lo termines manualmente:
para tipear más comandos o abres una nueva terminal (y no te olvides de activar
tu virtualenv allí también), o frena el servidor web yendo a la consola en la
que está corriendo y presionando Ctrl+C - las teclas Control y C juntas (en
Windows, deberás presionar Ctrl + Break).

> ¡Felicitaciones! ¡Has creado tu primer sitio web y lo has ejecutado usando un
servidor web! ¿No es genial?

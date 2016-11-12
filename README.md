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

## Instalar Django

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

## Comenzar un proyecto

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

## Configuración

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

## Iniciar servidor

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

# Modelo

> Hay un concepto en el mundo de la programación llamado programación orientada
a objetos. La idea es que en lugar de escribir todo como una aburrida
secuencia de instrucciones de programación podemos modelar cosas y definir
cómo interactúan con las demás.

> Entonces ¿Qué es un objeto? Es un conjunto de propiedades y acciones. Suena
raro, pero te daremos un ejemplo.

> [ver más en DjangoGirls](https://tutorial.djangogirls.org/es/django_models/)

Siguiendo con la explicación que realiza DjangoGirls:

> Un modelo en Django es un tipo especial de objeto que se guarda en la base de
datos. Una base de datos es una colección de datos. Allí es el lugar en el cual
almacenarás la información sobre usuarios, posts del blog, etc. Utilizaremos una
base de datos SQLite para almacenar nuestros datos. Este es el adaptador de base
de datos predeterminada en Django

> Piensa en el modelo en la base de datos como una hoja de cálculo con columnas
(campos) y filas (datos).

# Aplicación

Para mantener todo en orden, crearemos una aplicación separada dentro de nuestro
proyecto. Es muy bueno tener todo organizado desde el principio. Para crear una
aplicación, necesitamos ejecutar el siguiente comando en la consola (dentro de
la carpeta de django-ejemplo donde está el archivo manage.py):

```bash
python manage.py startapp lista_tareas
```

Vamos a crear una especie de lista de tareas. En [la guía de
DjangoGirls](https://tutorial.djangogirls.org/es/django_models/) crean un blog a
modo de ejemplo.

La estructura de nuestro proyecto debería quedar como sigue:

```
.
├── db.sqlite3
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   ├── pip-selfcheck.json
│   └── pyvenv.cfg
├── lista_tareas
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
├── misitio
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── README.md
└── requirements.txt

9 directories, 16 files
```

> Después de crear una aplicación también necesitamos decirle a Django que debe
utilizarla. Lo hacemos en el archivo mysite/settings.py. Tenemos que encontrar
*INSTALLED_APPS* y añadir una línea que contenga 'lista_tareas' (nombre que le
dimos a nuestra aplicación). El producto final debe tener este aspecto:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lista_tareas',
]
```

# Creando nuestros modelos
En el archivo *blog/models.py* definimos todos los objetos llamados Models.

Si los abrimos vamos a ver algo como esto:

```python
from django.db import models

# Create your models here.
```

Quitamos todo y escribimos un código como este:

```python
from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
```

Para una excelente explicación, te vuelvo a recomendar
[esta](https://tutorial.djangogirls.org/es/django_models/) sección de la página
de DjangoGirl donde podrás entender cada uno de los conceptos utilizados.

## Crear tablas para los modelos en tu base de datos

El último paso es añadir nuestro nuevo modelo a nuestra base de datos. Primero
tenemos que hacer que Django sepa que tenemos algunos cambios en nuestro modelo
(acabamos de crearlo), por eso escribiremos:

```python
python manage.py makemigrations lista_tareas
```

Django preparará un archivo de migración que tenemos que aplicar ahora a nuestra
base de datos. Escribiendo:

```python
python manage.py migrate lista_tareas
```

Nuestro modelo de **Tarea** está ahora en nuestra base de datos.

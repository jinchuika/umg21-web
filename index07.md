Alternativas a Django (Python):

- Ruby on Rails (Ruby)
- JSP (Java)
- Laravel (PHP)
- .NET MVC (C#)

Conceptos genéricos:

- Modelo: es la representación de una tabla en la base de datos.
- ORM: componente que utiliza la base de datos desde el lenguaje de programación elegido.
    - No tienen que escribir SQL
    - Suele estar mejor optimizado
    - Podemos cambiar de base de datos, sin cambiar las consultas en nuestro sistema
- Migraciones: registro de un cambio en la base de datos.


# Paso 1.

- Entrar a la carpeta del sistema
- Ejecutar el servidor con 
python .\manage.py runserver

# Paso 2

- Crear app con 
python manage.py startapp taller
- "Instalar aplicación"
    - vamos al archivo sistema/settings.py y buscamos donde dice INSTALLED_APPS
    - agregar el app de 'taller' en una nueva línea


# Paso 3
- Crear super usuario con
python .\manage.py createsuperuser

ponemos datos usuario - administrador


# Paso 4: crear base de datos
- Vamos a ir al archivo taller/models.py

# Paso 5: crear migraciones
python .\manage.py makemigrations taller

# Paso 6: aplicar migraciones
python .\manage.py migrate taller

# Paso 7: agregar al admin

en el archivo taller/admin.py

from django.contrib import admin
from .models import Cliente

admin.site.register(Cliente)

# Paso 8: Crear nuevo modelo
EN EL ARCHIVO taller/models.py
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=256)
    nit = models.CharField(max_length=12)
    telefono = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.nombre


class Vehiculo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    marca = models.CharField(max_length=32)
    modelo = models.IntegerField()


# Paso 9: aplicar migraciones

python manage.py makemigrations
python manage.py migrate

# Paso 10: agregar el nuevo modelo al administrador

Modificar taller/admin.py
from django.contrib import admin
from .models import Cliente, Vehiculo

admin.site.register(Cliente)
admin.site.register(Vehiculo)

# Paso 11: levantar el servidor
Empezamos pronto, mientras tanto:

# Paso 1

Descargar la versión más reciente del proyecto

https://github.com/jinchuika/umg21-web

# Paso 2

Ejecutar el servidor en la carpeta (cd sistema) del proyecto con

python manage.py runserver

# Paso 3

Creación de CRUD

Create
Read
Update
Delete

# Paso 4 

Hacer la parte de READ

Crear controlador en views.py:

class VehiculoListView(ListView):
    model = Vehiculo
    template_name = 'vehiculo_list.html'


Agregar un acceso en las URL (urls.py):

path('vehiculo/', views.VehiculoListView.as_view(), name='vehiculo_list'),

Crear un template en templates/vehiculo_list.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Listado de vehiculos</title>
</head>
<body>
    <h1>Listado de vehiculos</h1>
    {% for vehiculo in vehiculo_list %}
    {{ vehiculo }}
    <br>
    {{ vehiculo.modelo }}
    <hr>
    {% endfor %}
</body>
</html>


# Paso 5

Hacer la parte de CREATE

Agregar un controlador en views.py

class VehiculoCreateView(CreateView):
    model = Vehiculo
    template_name = 'vehiculo_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('vehiculo_list')

Agregar una URL:

path('vehiculo/add/', views.VehiculoCreateView.as_view(), name='vehiculo_add'),

Crear nuestro template (templates/vehiculo_form.html):

<h1>Ingrese los datos del vehiculo</h1>

<form action="{{ action }}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Guardar vehiculo</button>
</form>


# Paso 6

Create el UPDATE

Agregar controlador en views.py

class VehiculoUpdateView(UpdateView):
    model = Vehiculo
    template_name = 'vehiculo_form.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('vehiculo_list')

Agregar url en urls.py

path('vehiculo/<int:pk>/edit/', views.VehiculoUpdateView.as_view(), name='vehiculo_update'),

Reutilizar el template

# Paso 7

Agregar el DELETE


Agregar controlador en views.py

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'vehiculo_delete.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('vehiculo_list')

Agregar URL en urls.py

path('vehiculo/<int:pk>/delete/', views.VehiculoDeleteView.as_view(), name='vehiculo_delete'),

Creamos el template en templates/vehiculo_delete.html

<h1 style="color: green;">Está seguro de eliminar el vehiculo {{ object }}</h1>

<form action="{{ action }}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Eliminar</button>
</form>


# Paso 8 (Extra)

Agregar READ (detalle)


Agregar controlador

class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'vehiculo_detail.html'

Agregar URL

path('vehiculo/<int:pk>/', views.VehiculoDetailView.as_view(), name='vehiculo_detail'),

Agregar la vista en templates/vehiculo_detail.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vehiculo</title>
</head>
<body>
    Cliente: {{ vehiculo.cliente }}
    <br>
    Marca: {{ vehiculo.marca }}
    <br>
    Modelo: {{ vehiculo.modelo }}
</body>
</html>


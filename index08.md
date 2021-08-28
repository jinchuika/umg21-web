# paso 1: aplicar migraciones
cd sistema
python manage.py migrate

# paso 2: crear usuario administrador 
python manage.py createsuperuser

# paso 3: aplicar migraciones
python manage.py runserver

# paso 4: entrar al admin
localhost:8000/admin

# paso 5: entrar al listado de clientes
localhost:8000/cliente

# nota:
Los templates son componentes de la vista que se usan para diseñar cómo va a interactuar el usuario con el sistema y cómo va a ver la información.

# paso 6: entrar a un cliente especifico
localhost:8000/cliente/ID_DEL_CLIENTE

# paso 7: crear cliente
localhost:8000/cliente/add/

para ver que funciona, van al listado de clientes

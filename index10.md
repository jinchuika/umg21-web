# paso 1

Descargar actualización

# paso 2

Descargar e instalar postgres
https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

Usar configuración por default.
Puerto: 5432

Agregar una conexión

# paso 3

Instalar el driver
pip install -U psycopg2-binary

# Paso 4

Crear una base de datos en postgres desde cualquier cliente

# paso 5

Ejecutar migraciones

cd sistema
python manage.py migrate

# paso 6

Crear super usuario
python manage.py createsuperuser

levantar servidor 
python manage.py runserver


# Resumen

1. Un framework web, por lo general se conecta a distintos tipos de base de datos
2. Al framework no debe importarle a qué base de datos nos conectamos
3. EL SERVIDOR WEB ES UN CLIENTE DEL SERVIDOR DE BASE DE DATOS
4. Para conectar el servidor web al servidor de DB se usa un driver

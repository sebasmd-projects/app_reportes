# app_reportes
Manejo de listview obteniendo valores desde metodo get

1. crear entorno virtual
python -m venv nombreDelEntorno

2. activar entorno virtual

3. instalar dependencias
pip install -r requirements.txt

Nota:
para linux y mac instalar psycopg2-binary y borrar el psycopg2
pip install psycopg2-binary

4. crear una base de datos en posgresql

5. abrir el archivo global_config.json y vincular los datos

6. con el entorno activo: 
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Configuración de la conexión a la base de datos (autenticación de Windows)
def obtener_conexion():
    conexion = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        ##
    )
    return conexion

# Contador de visitas
contador_visitas = 0

##
def index():
    global contador_visitas
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        hobby = request.form['hobby']
	vistas = request. form ['vistas']
        
        # Insertar los datos en la base de datos
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        query = "mantenDatosTaller @op='nuevo', @nombre=?, @edad=?, @hobby=?, @vistas=?"
        cursor.execute(query, (nombre, edad, hobby))
        conexion.commit()
        cursor.close()
        conexion.close()
        
        contador_visitas += 1
        return render_template('index.html', nombre=nombre, edad=edad, hobby=hobby, contador=contador_visitas)
    
    return render_template('index.html', contador=contador_visitas)

# Nueva ruta para mostrar usuarios registrados
##
def mostrar_usuarios():
    # Obtener los datos de la base de datos
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    query = "mantenDatosTaller @op='verT', @nombre='', @edad='', @hobby='', @vistas=''"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()

    # Convertir los datos a un formato más amigable para Jinja
    lista_usuarios = []
    for usuario in usuarios:
        lista_usuarios.append({
            'nombre': usuario[0],
            'edad': usuario[1],
            'hobby': usuario[2],
            'vistas': usuario[3]
        })

    # Renderizar el template y pasarle los usuarios
    return render_template('usuarios.html', usuarios=lista_usuarios)

if __name__ == '__main__':
    ##
    (debug=True)

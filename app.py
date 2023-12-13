
from flask import Flask, render_template, jsonify, request, url_for
from os import path
import pymysql
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app = Flask(__name__, static_url_path='/static')


# Configura los detalles de la conexión a MySQL
host = 'localhost'
usuario = 'root'
contrasena = '2305'
base_de_datos = 'vorx'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administrador.html')
def listaClientes():
    return render_template('administrador.html')

@app.route('/buzo.html')
def buzo():
    return render_template('buzo.html')

@app.route('/crearcuenta.html')
def crearcuenta():
    return render_template('crearcuenta.html')

@app.route('/nosotros.html')
def nosotros():
    return render_template('nosotros.html')

@app.route('/productos.html')
def productos():
    return render_template('productos.html')

@app.route('/remeras.html')
def remeras():
    return render_template('remeras.html')



def conectar_db():
    conexion = pymysql.connect(
        host=host,
        user=usuario,
        password=contrasena,
        db=base_de_datos,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conexion

@app.route('/administrador.html', methods=['GET'])
def listadoClientes():
    # Crea la conexión
    conexion = conectar_db()
    cursor = conexion.cursor()

    try:
        # Crea un objeto cursor para ejecutar consultas
        with conexion.cursor() as cursor:
            # Ejecuta una consulta (modifica según tus necesidades)
            sql = "SELECT * FROM vorx.cliente;"
            cursor.execute(sql)

            # Obtiene los resultados
            resultados = cursor.fetchall()
            
            clientes_json = [] # ESTO ES UNA LISTA DE DICCIONARIOS
    
            for resultado in resultados:
                cliente_json = { # ESTO ES UN DICCIONARIO
                    "Id_Cliente": resultado[0],
                    "Nombre": resultado[1],
                    "Email": resultado[2],
                    "Genero": resultado[3],
                 
                }
                clientes_json.append(cliente_json)
            return jsonify(clientes_json), 200
    finally:
       conexion.close()
       
       


    # Renderiza la plantilla HTML con los resultados de la consulta
#return render_template('administrador.html', resultados=resultados)


@app.route('/crearcuenta.html', methods=['POST'])
def crear():
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()

        nombre = request.form['Nombre']
        email = request.form['Email']
        fecha_nacimiento = request.form['Fecha_Nacimiento']
        genero = request.form.get('Genero', '')

        # Inserta los datos en la base de datos
        with conexion.cursor() as cursor:
            sql1 = "INSERT INTO `vorx`.`cliente`(`Nombre`, `Email`, `Genero`, `Fecha_Nacimiento`) VALUES (%s, %s, %s, %s);"
            cursor.execute(sql1, (nombre, email, genero, fecha_nacimiento))
            conexion.commit()

    except Exception as e:
        print("Error:", e)
    finally:
        if conexion:
            conexion.close()

    # Renderiza la plantilla HTML con los resultados de la consulta
    return render_template('crearcuenta.html')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
"""
from flask import Flask, render_template, request, url_for, jsonify

from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

host = 'localhost'
usuario = 'root'
contrasena = '2305'
base_de_datos = 'vorx'
# conexión a base de datos
def conectar_db():
    conexion = pymysql.connect(
        host=host,
        user=usuario,
        password=contrasena,
        db=base_de_datos,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conexion


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/administrador.html')
def listaClientes():
    return render_template('administrador.html')

@app.route("/administrador.html", methods=["GET"])
def listadoClientes():
    
    conexion = conectar_db()
    cursor = conexion.cursor()

    try:
        # Crea un objeto cursor para ejecutar consultas
        with conexion.cursor() as cursor:
            # Ejecuta una consulta (modifica según tus necesidades)
            sql = "SELECT * FROM vorx.cliente"
            cursor.execute(sql)

            # Obtiene los resultados
            data = cursor.fetchall()

    finally:
        # Cierra la conexión
        conexion.close()

    # Renderiza la plantilla HTML con los resultados de la consulta
    return render_template('administrador.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
"""
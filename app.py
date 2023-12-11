"""
from flask import Flask, render_template, jsonify
from os import path
import pymysql

app = Flask(__name__, template_folder='templates')
app = Flask(__name__, static_url_path='/static')


# Configura los detalles de la conexión a MySQL
host = 'localhost'
usuario = 'root'
contrasena = '2305'
base_de_datos = 'vorx'

@app.route('/')
def index():
    # Crea la conexión
    conexion = pymysql.connect(
        host=host,
        user=usuario,
        password=contrasena,
        db=base_de_datos,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        # Crea un objeto cursor para ejecutar consultas
        with conexion.cursor() as cursor:
            # Ejecuta una consulta (modifica según tus necesidades)
            sql = "SELECT * FROM vorx.cliente"
            cursor.execute(sql)

            # Obtiene los resultados
            resultados = cursor.fetchall()

    finally:
        # Cierra la conexión
        conexion.close()

    # Renderiza la plantilla HTML con los resultados de la consulta
    return render_template('administrador.html', resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
"""
from flask import Flask, render_template, jsonify, request, redirect, url_for
import pymysql

app = Flask(__name__, template_folder='templates', static_url_path='/static')

# Configura los detalles de la conexión a MySQL
host = 'localhost'
usuario = 'root'
contrasena = '2305'
base_de_datos = 'vorx'

@app.route('/')
def index():
    conexion = pymysql.connect(
        host=host,
        user=usuario,
        password=contrasena,
        db=base_de_datos,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM vorx.cliente"
            cursor.execute(sql)
            resultados = cursor.fetchall()

    finally:
        conexion.close()

    return render_template('administrador.html', resultados=resultados)

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']

        conexion = pymysql.connect(
            host=host,
            user=usuario,
            password=contrasena,
            db=base_de_datos,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with conexion.cursor() as cursor:
                sql = "INSERT INTO vorx.cliente (Nombre, Email) VALUES (%s, %s)"
                cursor.execute(sql, (nombre, email))
                conexion.commit()

        finally:
            conexion.close()

    return redirect(url_for('index'))

@app.route('/editar_cliente/<int:cliente_id>', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    conexion = pymysql.connect(
        host=host,
        user=usuario,
        password=contrasena,
        db=base_de_datos,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conexion.cursor() as cursor:
            if request.method == 'POST':
                nombre = request.form['nombre']
                email = request.form['email']

                sql = "UPDATE vorx.cliente SET Nombre=%s, Email=%s WHERE id=%s"
                cursor.execute(sql, (nombre, email, cliente_id))
                conexion.commit()

            sql = "SELECT * FROM vorx.cliente WHERE id=%s"
            cursor.execute(sql, cliente_id)
            cliente = cursor.fetchone()

    finally:
        conexion.close()

    return render_template('editar_cliente.html', cliente=cliente)

@app.route('/eliminar_cliente/<int:cliente_id>')
def eliminar_cliente(cliente_id):
    conexion = pymysql.connect(
        host=host,
        user=usuario,
        password=contrasena,
        db=base_de_datos,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM vorx.cliente WHERE id=%s"
            cursor.execute(sql, cliente_id)
            conexion.commit()

    finally:
        conexion.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=4000)
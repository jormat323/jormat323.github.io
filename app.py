from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
DATABASE = 'consultas.db'

def obtener_conexion():
    return sqlite3.connect(DATABASE)

def guardar_consulta(nombre, email, consulta):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO consultas (nombre, email, consulta) VALUES (?, ?, ?)", (nombre, email, consulta))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html') # Asegúrate de que tu archivo HTML se llame 'index.html' y esté en la misma carpeta o en una carpeta 'templates'

@app.route('/registrar_consulta', methods=['POST'])
def registrar_consulta():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        consulta = request.form['consulta']
        guardar_consulta(nombre, email, consulta)
        return "¡Consulta registrada con éxito!" # Puedes redirigir a una página de agradecimiento si lo deseas

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

import requests

app = Flask(__name__)

API_URL = "http://40.118.66.81/api/"
GET_URL = API_URL + "listar_archivos"
PUT_URL = API_URL + "actualizar_archivo/"

@app.route("/", methods=["GET"])
def home():
    # Obtener la lista de archivos desde la API
    response = requests.get(GET_URL)
    archivos = response.json()["archivos"]

    # Renderizar la plantilla de HTML
    return render_template("index.html", archivos=archivos)

@app.route("/update", methods=["POST"])
def update():
    # Obtener el ID del archivo seleccionado desde el formulario
    archivo_id = request.form["archivo_id"]

    # Hacer la llamada a la API de actualización de archivos
    response = requests.put(PUT_URL + archivo_id)

    # Redirigir a la página de inicio
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()

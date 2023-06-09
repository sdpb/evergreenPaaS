from flask import Flask, render_template, request, redirect, url_for
import requests
import json

app = Flask(__name__)


API_URL = "http://40.118.66.81/api"
LISTAR_ARCHIVOS_ENDPOINT = "/listar_archivos"
ACTUALIZAR_ARCHIVO_ENDPOINT = "/actualizar_archivo"

@app.route('/')
def index():
    # Hacemos un llamado a la API para obtener la lista de archivos
    response = requests.get(API_URL + LISTAR_ARCHIVOS_ENDPOINT)
    archivos = json.loads(response.text)['archivos']
    return render_template('index.html', archivos=archivos)

@app.route('/cambiar_nombre', methods=['POST'])
def cambiar_nombre():
    # Obtenemos el id del archivo y el nuevo nombre del formulario
    archivo_id = request.form['archivo_oid']
    nuevo_nombre = request.form['nuevo_nombre']
    # Armamos la url para llamar a la API de actualizar archivo
    url = f'{API_URL}{ACTUALIZAR_ARCHIVO_ENDPOINT}/{archivo_id}'
    # Armamos el payload con el nuevo nombre
    payload = {"nuevo_nombre": nuevo_nombre}
    headers = {"Content-Type": "application/json"}
    response = requests.put(url, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return f"Error al cambiar el nombre del archivo con id {archivo_id}"

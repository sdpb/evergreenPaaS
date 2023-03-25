from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Consumir la API para obtener la lista de archivos
    response = requests.get(f"{os.environ['API_URL']}/api/listar_archivos")
    archivo_lista = response.json()

    return render_template('index.html', archivo_lista=archivo_lista)

@app.route('/actualizar_archivo', methods=['POST'])
def actualizar_archivo():
    archivo_id = request.form['archivo_id']
    archivo_nuevo_nombre = request.form['archivo_nuevo_nombre']

    # Validar que se ingresó un ID y un nuevo nombre
    if not archivo_id or not archivo_nuevo_nombre:
        return jsonify({'error': 'Por favor ingresa el ID del archivo y el nuevo nombre.'}), 400

    # Construir la solicitud PUT
    put_data = {'nombre': archivo_nuevo_nombre}
    response = requests.put(f"{os.environ['API_URL']}/api/actualizar_archivo/{archivo_id}", json=put_data)

    if response.status_code == 200:
        return jsonify({'mensaje': f"El nombre del archivo con ID {archivo_id} fue actualizado exitosamente a {archivo_nuevo_nombre}."}), 200
    else:
        return jsonify({'error': 'Hubo un error al actualizar el nombre del archivo.'}), 500

if __name__ == '__main__':
    app.run()

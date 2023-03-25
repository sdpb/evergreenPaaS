const archivoLista = document.getElementById("archivo-lista");

// Consumir la API para obtener la lista de archivos
// fetch(`${process.env.API_URL}/api/listar_archivos`)
fetch(`http://40.118.66.81/api/listar_archivos`)
  .then(response => response.json())
  .then(data => {
    data.forEach(archivo => {
      const li = document.createElement("li");
      li.innerText = `${archivo.id} - ${archivo.nombre}`;
      li.addEventListener("click", () => seleccionarArchivo(archivo.id));
      archivoLista.appendChild(li);
    });
  })
  .catch(error => console.error(error));

function seleccionarArchivo(id) {
  const archivoIdInput = document.createElement("input");
  archivoIdInput.type = "hidden";
  archivoIdInput.id = "archivo-id";
  archivoIdInput.value = id;
  document.body.appendChild(archivoIdInput);
}

function actualizarArchivo() {
  const archivoId = document.getElementById("archivo-id").value;
  const archivoNuevoNombre = document.getElementById("archivo-nuevo-nombre").value;

  // Validar que se ingresó un ID y un nuevo nombre
  if (!archivoId || !archivoNuevoNombre) {
    alert("Por favor ingresa el ID del archivo y el nuevo nombre.");
    return;
  }

  // Construir la solicitud PUT
  const requestOptions = {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nombre: archivoNuevoNombre })
  };

  // Consumir la API para actualizar el nombre del archivo
  fetch(`${process.env.API_URL}/api/actualizar_archivo/${archivoId}`, requestOptions)
    .then(response => response.json())
    .then(data => {
      alert(`El nombre del archivo con ID ${data.id} fue actualizado exitosamente a ${data.nombre}.`);
    })
    .catch(error => console.error(error));
}


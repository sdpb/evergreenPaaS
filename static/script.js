const formularioActualizar = document.getElementById('formulario-actualizar');

formularioActualizar.addEventListener('submit', (event) => {
  event.preventDefault();

  const archivoId = document.getElementById('archivo-id').value;
  const archivoNuevoNombre = document.getElementById('archivo-nuevo-nombre').value;

  // Validar que se ingresó un ID y un nuevo nombre
  if (!archivoId || !archivoNuevoNombre) {
    alert('Por favor ingresa el ID del archivo y el nuevo nombre.');
    return;
  }

  // Construir la solicitud POST
  const data = new FormData();
  data.append('archivo_id', archivoId);
  data.append('archivo_nuevo_nombre', archivoNuevoNombre);

  fetch('/actualizar_archivo', {
    method: 'POST',
    body: data
  })
  .then(response => response.json())
  .then(data => {
    if (data.error) {
      alert(data.error);
    } else {
      alert(data.mensaje);
    }
  })
  .catch(error => {
    alert('Hubo un error al actualizar el nombre del archivo.');
  });
});

const API_BASE_URL = "https://api.restful-api.dev/objects";

async function getUserById(id) {
  const response = await axios.get(`${API_BASE_URL}/${encodeURIComponent(id)}`);
  return response.data;
}

async function createUser(userData) {
  const response = await axios.post(API_BASE_URL, userData);
  return response.data;
}

async function patchUser(id, partialData) {
  const response = await axios.patch(
    `${API_BASE_URL}/${encodeURIComponent(id)}`,
    partialData
  );
  return response.data;
}

function getApiErrorMessage(error) {
  if (error.response) {
    if (error.response.status === 404) return "No se encontró el usuario.";
    if (error.response.status === 401) return "La solicitud no está autorizada.";
    if (error.response.status >= 500) return "Error del servidor. Inténtalo más tarde.";
    return `La solicitud falló (HTTP ${error.response.status}).`;
  }
  if (error.request) return "No se recibió respuesta del servidor. Comprueba tu conexión.";
  return error.message || "Ocurrió un error inesperado.";
}

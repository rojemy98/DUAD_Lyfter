
const SESSION_KEY = "practiceUserSession";
const SESSION_DURATION = 5 * 60 * 1000; // 5 minutos
const FLASH_MESSAGE_KEY = "sessionFlashMessage";

// Guardar el ID y el timestamp al iniciar sesión
function saveSession(user) {
  const session = {
    id: user.id,
    loginTimestamp: Date.now()
  };

  localStorage.setItem(SESSION_KEY, JSON.stringify(session));
}

// Obtener la sesión almacenada
function getSession() {
  try {
    const value = localStorage.getItem(SESSION_KEY);
    return value ? JSON.parse(value) : null;
  } catch {
    return null;
  }
}

// Comprobar si la sesión ha expirado
function isSessionExpired(session) {
  if (!session || typeof session.loginTimestamp !== "number") {
    return true;
  }

  return Date.now() - session.loginTimestamp > SESSION_DURATION;
}

// Eliminar la sesión
function clearSession() {
  localStorage.removeItem(SESSION_KEY);
}

// Guardar un mensaje para mostrarlo después de redirigir al login
function setFlashMessage(message) {
  sessionStorage.setItem(FLASH_MESSAGE_KEY, message);
}

// Recuperar y eliminar el mensaje temporal
function consumeFlashMessage() {
  const message = sessionStorage.getItem(FLASH_MESSAGE_KEY);
  sessionStorage.removeItem(FLASH_MESSAGE_KEY);
  return message;
}

// Proteger páginas que requieren una sesión válida
function requireLogin() {
  const session = getSession();

  if (!session) {
    window.location.replace("login.html");
    return false;
  }

  if (isSessionExpired(session)) {
    clearSession();

    setFlashMessage(
      "Sesión expirada, vuelva a iniciar sesión"
    );

    window.location.replace("login.html");
    return false;
  }

  return true;
}

// Evitar que un usuario con sesión válida vuelva al login
function redirectIfLoggedIn() {
  const session = getSession();

  if (!session) {
    return false;
  }

  if (isSessionExpired(session)) {
    clearSession();

    setFlashMessage(
      "Sesión expirada, vuelva a iniciar sesión"
    );

    return false;
  }

  window.location.replace("perfil.html");
  return true;
}

// Mostrar mensajes en el DOM
function setMessage(element, message, type = "") {
  element.textContent = message;
  element.className = `message ${type}`.trim();
}

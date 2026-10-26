const SESSION_KEY = "practiceUserSession";
const FLASH_MESSAGE_KEY = "sessionFlashMessage";
const SESSION_TIMEOUT = 5 * 60 * 1000;

// Guardar los datos del usuario al iniciar sesión
function saveSession(user) {
  const session = {
    id: user.id,
    name: user.name,
    email: user.email,
    loginTime: Date.now(),
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

// Eliminar la sesión
function clearSession() {
  localStorage.removeItem(SESSION_KEY);
}

// Guardar un mensaje para mostrarlo después de redirigir
function setFlashMessage(message) {
  sessionStorage.setItem(FLASH_MESSAGE_KEY, message);
}

// Recuperar y eliminar el mensaje temporal
function consumeFlashMessage() {
  const message = sessionStorage.getItem(FLASH_MESSAGE_KEY);
  sessionStorage.removeItem(FLASH_MESSAGE_KEY);
  return message;
}

// Proteger páginas que requieren una sesión
function requireLogin() {
  const session = getSession();

  if (!session || !session.id) {
    clearSession();
    window.location.replace("login.html");
    return false;
  }

  const elapsedTime = Date.now() - session.loginTime;

  if (!Number.isFinite(session.loginTime) || elapsedTime > SESSION_TIMEOUT) {
    clearSession();

    setFlashMessage("Sesión expirada, vuelva a iniciar sesión");

    window.location.replace("login.html");
    return false;
  }

  return true;
}

// Evitar que un usuario con sesión válida vuelva al login
function redirectIfLoggedIn() {
  const session = getSession();

  if (!session || !session.id) {
    clearSession();
    return false;
  }

  const elapsedTime = Date.now() - session.loginTime;

  if (!Number.isFinite(session.loginTime) || elapsedTime > SESSION_TIMEOUT) {
    clearSession();

    setFlashMessage("Sesión expirada, vuelva a iniciar sesión");

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

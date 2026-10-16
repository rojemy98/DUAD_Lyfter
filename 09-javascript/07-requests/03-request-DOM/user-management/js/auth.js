const SESSION_KEY = "practiceUserSession";

function saveSession(user) {
  localStorage.setItem(SESSION_KEY, JSON.stringify({ id: user.id }));
}

function getSession() {
  try {
    const value = localStorage.getItem(SESSION_KEY);
    return value ? JSON.parse(value) : null;
  } catch {
    return null;
  }
}

function clearSession() {
  localStorage.removeItem(SESSION_KEY);
}

function requireLogin() {
  const session = getSession();
  if (!session || !session.id) {
    window.location.replace("login.html");
    return false;
  }
  return true;
}

function redirectIfLoggedIn() {
  const session = getSession();
  if (session && session.id) {
    window.location.replace("perfil.html");
    return true;
  }
  return false;
}

function setMessage(element, message, type = "") {
  element.textContent = message;
  element.className = `message ${type}`.trim();
}

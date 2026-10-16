document.addEventListener("DOMContentLoaded", async () => {
  if (!requireLogin()) return;

  const message = document.querySelector("#message");
  const cards = document.querySelector("#profile-cards");
  const logoutButton = document.querySelector("#logout-button");
  const session = getSession();

  logoutButton.addEventListener("click", () => {
    clearSession();
    window.location.replace("login.html");
  });

  setMessage(message, "Cargando perfil...");

  try {
    const user = await getUserById(session.id);

    // No mostrar la contraseña en el perfil.
    const fields = {
      "ID de usuario": user.id,
      "Nombre": user.data?.name ?? user.name ?? "No especificado",
      "Correo electrónico": user.data?.email ?? "No especificado"
    };

    cards.replaceChildren();
    Object.entries(fields).forEach(([label, value]) => {
      const card = document.createElement("article");
      card.className = "card";

      const heading = document.createElement("p");
      heading.className = "card-label";
      heading.textContent = label;

      const content = document.createElement("p");
      content.className = "card-value";
      content.textContent = String(value);

      card.append(heading, content);
      cards.appendChild(card);
    });

    setMessage(message, "");
  } catch (error) {
    clearSession();
    setMessage(message, `No se pudo cargar el perfil. ${getApiErrorMessage(error)}`, "error");
    window.setTimeout(() => window.location.replace("login.html"), 1800);
  }
});


document.addEventListener("DOMContentLoaded", async () => {
  if (!requireLogin()) return;

  const message = document.querySelector("#message");
  const cards = document.querySelector("#profile-cards");
  const logoutButton = document.querySelector("#logout-button");
  const editButton = document.querySelector("#edit-profile-button");
  const editForm = document.querySelector("#edit-profile-form");
  const cancelButton = document.querySelector("#cancel-edit-button");
  const saveButton = document.querySelector("#save-profile-button");

  const session = getSession();
  let currentUser = null;

  // Cerrar sesión
  logoutButton.addEventListener("click", () => {
    clearSession();
    window.location.replace("login.html");
  });

  // Mostrar el formulario con los datos actuales
  editButton.addEventListener("click", () => {
    if (!currentUser) return;

    editForm.elements.name.value =
      currentUser.data?.name ?? currentUser.name ?? "";

    editForm.elements.address.value =
      currentUser.data?.address ?? "";

    editForm.classList.remove("hidden");
    editForm.elements.name.focus();

    setMessage(message, "");
  });

  // Cancelar la edicion
  cancelButton.addEventListener("click", () => {
    editForm.reset();
    editForm.classList.add("hidden");
    setMessage(message, "");
  });

  // Guardar los cambios
  editForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    if (!currentUser) return;

    const name = editForm.elements.name.value.trim();
    const address = editForm.elements.address.value.trim();

    if (!name || !address) {
      setMessage(
        message,
        "El nombre y la dirección son obligatorios.",
        "error"
      );
      return;
    }

    saveButton.disabled = true;
    saveButton.textContent = "Guardando...";
    setMessage(message, "");

    try {
      // Conservar los demas datos del usuario
      const updatedData = {
        ...(currentUser.data || {}),
        name,
        address
      };

      // PATCH: actualizar los datos del usuario
      const apiResult = await patchUser(currentUser.id, {
        data: updatedData
      });

      // Actualizar el objeto local con los cambios
      currentUser = {
        ...currentUser,
        ...(apiResult || {}),
        data: {
          ...(currentUser.data || {}),
          ...(apiResult?.data || {}),
          name,
          address
        }
      };

      // Actualizar las tarjetas del DOM
      renderProfile(currentUser, cards);

      editForm.classList.add("hidden");

      setMessage(
        message,
        "¡Perfil actualizado correctamente!",
        "success"
      );

    } catch (error) {
      setMessage(
        message,
        `No se pudo actualizar el perfil. ${getApiErrorMessage(error)}`,
        "error"
      );

    } finally {
      saveButton.disabled = false;
      saveButton.textContent = "Guardar";
    }
  });

  // Consultar y mostrar los datos del usuario
  try {
    setMessage(message, "Cargando perfil...");

    currentUser = await getUserById(session.id);

    renderProfile(currentUser, cards);

    setMessage(message, "");

  } catch (error) {
    clearSession();

    setMessage(
      message,
      `No se pudo cargar el perfil. ${getApiErrorMessage(error)}`,
      "error"
    );

    window.setTimeout(() => {
      window.location.replace("login.html");
    }, 1800);
  }
});


// Crear las tarjetas del perfil
function renderProfile(user, cards) {
  // Nunca mostrar la contraseña en pantalla
  const fields = {
    "ID de usuario": user.id,
    "Nombre": user.data?.name ?? user.name ?? "No especificado",
    "Correo electrónico": user.data?.email ?? "No especificado",
    "Dirección": user.data?.address ?? "No especificada"
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
}


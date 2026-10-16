document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector("#password-form");
  const message = document.querySelector("#message");
  const submitButton = form.querySelector('button[type="submit"]');
  const session = getSession();

  if (session && session.id) {
    form.elements.userId.value = session.id;
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    setMessage(message, "");

    const id = form.elements.userId.value.trim();
    const oldPassword = form.elements.oldPassword.value;
    const newPassword = form.elements.newPassword.value;
    const confirmPassword = form.elements.confirmPassword.value;

    if (!id) {
      setMessage(message, "Debes ingresar el ID del usuario.", "error");
      return;
    }

    if (!oldPassword || !newPassword || !confirmPassword) {
      setMessage(message, "Completa todos los campos.", "error");
      return;
    }

    if (newPassword !== confirmPassword) {
      setMessage(message, "La nueva contraseña y su confirmación no coinciden.", "error");
      return;
    }

    if (newPassword === oldPassword) {
      setMessage(message, "La nueva contraseña debe ser diferente de la anterior.", "error");
      return;
    }

    submitButton.disabled = true;
    submitButton.textContent = "Actualizando...";

    try {
      // 1. GET: traer el usuario y comprobar que exista.
      const user = await getUserById(id);

      // 2. Validar la contraseña anterior.
      if (!user.data || user.data.password !== oldPassword) {
        setMessage(message, "La contraseña anterior es incorrecta.", "error");
        return;
      }

      // 3. PATCH: enviar únicamente el campo que cambia dentro de data.
      await patchUser(id, {
        data: {
          password: newPassword
        }
      });

      setMessage(message, "¡Contraseña actualizada correctamente!", "success");
      form.elements.oldPassword.value = "";
      form.elements.newPassword.value = "";
      form.elements.confirmPassword.value = "";
    } catch (error) {
      if (error.response && error.response.status === 404) {
        setMessage(message, "No existe un usuario con ese ID.", "error");
      } else {
        setMessage(message, `No se pudo cambiar la contraseña. ${getApiErrorMessage(error)}`, "error");
      }
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = "Actualizar contraseña";
    }
  });
});

document.addEventListener("DOMContentLoaded", () => {
  if (redirectIfLoggedIn()) return;

  const form = document.querySelector("#register-form");
  const message = document.querySelector("#message");
  const submitButton = form.querySelector('button[type="submit"]');

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    setMessage(message, "");

    const name = form.elements.name.value.trim();
    const email = form.elements.email.value.trim();
    const password = form.elements.password.value;

    if (!name || !email || !password) {
      setMessage(message, "Completa todos los campos.", "error");
      return;
    }

    submitButton.disabled = true;
    submitButton.textContent = "Creando cuenta...";

    try {
      const user = await createUser({
        name: "Practice User",
        data: { name, email, password }
      });

      if (!user || !user.id) {
        throw new Error("El API no devolvió un ID para el usuario creado.");
      }

      saveSession(user);
      alert(`Usuario creado correctamente! Tu id es ${user.id}`);
      window.location.href = "perfil.html";
    } catch (error) {
      setMessage(message, `No se pudo crear el usuario. ${getApiErrorMessage(error)}`, "error");
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = "Crear cuenta";
    }
  });
});

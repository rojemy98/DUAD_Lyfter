document.addEventListener("DOMContentLoaded", () => {
    if (redirectIfLoggedIn()) return;

    const form = document.querySelector("#login-form");
    const message = document.querySelector("#message");
    const submitButton = form.querySelector('button[type="submit"]');

    // Mostrar el mensaje enviado desde una página protegida
    const flashMessage = consumeFlashMessage();

    if (flashMessage) {
        setMessage(message, flashMessage, "error");
    }

    form.addEventListener("submit", async (event) => {
        event.preventDefault();
        setMessage(message, "");

        const id = form.elements.userId.value.trim();
        const password = form.elements.password.value;

        if (!id || !password) {
            setMessage(message, "Ingresa tu ID y contraseña.", "error");
            return;
        }

        submitButton.disabled = true;
        submitButton.textContent = "Verificando...";

        try {
            const user = await getUserById(id);
            const storedPassword = user && user.data && user.data.password;

            if (!storedPassword || storedPassword !== password) {
                setMessage(
                    message,
                    "El ID no existe o la contraseña es incorrecta.",
                    "error"
                );
                return;
            }

            saveSession(user);
            window.location.href = "perfil.html";

        } catch (error) {
            if (error.response && error.response.status === 404) {
                setMessage(
                    message,
                    "El usuario no existe o el ID es incorrecto.",
                    "error"
                );
            } else {
                setMessage(message, getApiErrorMessage(error), "error");
            }
        } finally {
            submitButton.disabled = false;
            submitButton.textContent = "Iniciar sesión";
        }
    });
});
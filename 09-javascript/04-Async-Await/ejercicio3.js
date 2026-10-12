
const userIdInput = document.getElementById("userId");
const searchButton = document.getElementById("searchButton");
const result = document.getElementById("result");

searchButton.addEventListener("click", async function () {
    const userId = userIdInput.value.trim();

    if (!userId || Number(userId) < 1) {
        result.textContent = "Please enter a valid user ID.";
        return;
    }

    result.textContent = "Loading...";

    try {
        const response = await fetch(
            `https://reqres.in/api/users/${userId}`
        );

        if (!response.ok) {
            throw new Error("User not found.");
        }

        const data = await response.json();
        const user = data.data;

        result.innerHTML = `
            <h3>User Information</h3>
            <p><strong>First name:</strong> ${user.first_name}</p>
            <p><strong>Last name:</strong> ${user.last_name}</p>
            <p><strong>Email:</strong> ${user.email}</p>
        `;

    } catch (error) {
        result.textContent = "Error: " + error.message;
    }
});

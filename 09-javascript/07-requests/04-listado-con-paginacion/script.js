
const API_URL = "https://api.restful-api.dev/objects";

const objectsContainer = document.getElementById("objects-container");
const statusElement = document.getElementById("status");
const previousBtn = document.getElementById("previous-btn");
const nextBtn = document.getElementById("next-btn");
const pageInfo = document.getElementById("page-info");

let allObjects = [];
let currentPage = 1;

const itemsPerPage = 5;

async function loadObjects() {
    try {
        const response = await axios.get(API_URL);

        allObjects = response.data;

        renderPage();
    } catch (error) {
        statusElement.textContent =
            "Error al cargar los objetos: " + error.message;
    }
}

function renderPage() {
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;

    const pageObjects = allObjects.slice(startIndex, endIndex);

    objectsContainer.innerHTML = "";

    pageObjects.forEach((object) => {
        const card = document.createElement("article");
        card.classList.add("object-card");

        const title = document.createElement("h2");
        title.textContent = object.name || "Sin nombre";

        const id = document.createElement("p");
        id.textContent = "ID: " + object.id;

        card.appendChild(title);
        card.appendChild(id);

        if (object.data) {
            const details = document.createElement("p");

            details.textContent =
                "Datos: " + JSON.stringify(object.data);

            card.appendChild(details);
        }

        objectsContainer.appendChild(card);
    });

    const totalPages = Math.ceil(
        allObjects.length / itemsPerPage
    );

    pageInfo.textContent =
        `Página ${currentPage} de ${totalPages}`;

    previousBtn.disabled = currentPage === 1;
    nextBtn.disabled = currentPage >= totalPages;

    statusElement.textContent =
        `Total de objetos: ${allObjects.length}`;
}

previousBtn.addEventListener("click", () => {
    if (currentPage > 1) {
        currentPage--;
        renderPage();
    }
});

nextBtn.addEventListener("click", () => {
    const totalPages = Math.ceil(
        allObjects.length / itemsPerPage
    );

    if (currentPage < totalPages) {
        currentPage++;
        renderPage();
    }
});

loadObjects();

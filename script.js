
const addRecipeBtn = document.getElementById("add-recipe-btn");
const recipeModal = document.getElementById("recipe-modal");
const closeModal = document.querySelector(".close");
const saveRecipeBtn = document.getElementById("save-recipe");
const recipesList = document.getElementById("recipes-list");
const searchInput = document.getElementById("search-input");
const categorySelect = document.getElementById("recipe-category");
const filterBtns = document.querySelectorAll(".filter-btn");


// ----- Funções LocalStorage -----
function saveRecipes(recipes) {
  localStorage.setItem("recipes", JSON.stringify(recipes));
}

function loadRecipes() {
  const saved = localStorage.getItem("recipes");
  return saved ? JSON.parse(saved) : [];
}

// ----- Renderizar receitas com animação -----
function renderRecipes(recipes) {
  recipesList.innerHTML = "";

  if (recipes.length === 0) {
    recipesList.innerHTML = "<p>Nenhuma receita encontrada.</p>";
    return;
  }

  recipes.forEach((recipe, index) => {
    const card = document.createElement("div");
    card.classList.add("recipe-card");

    if (recipe.image) {
      const img = document.createElement("img");
      img.src = recipe.image;
      card.appendChild(img);
    }

    const name = document.createElement("h3");
    name.textContent = recipe.name;
    card.appendChild(name);

    const cat = document.createElement("p");
    cat.textContent = `Categoria: ${recipe.category}`;
    card.appendChild(cat);

    const ing = document.createElement("p");
    ing.textContent = `Ingredientes: ${recipe.ingredients}`;
    card.appendChild(ing);

    const steps = document.createElement("p");
    steps.textContent = `Modo de preparo: ${recipe.steps}`;
    card.appendChild(steps);

    const removeBtn = document.createElement("button");
    removeBtn.textContent = "🗑️ Excluir";
    removeBtn.classList.add("remove-btn");
    removeBtn.addEventListener("click", () => {
      recipes.splice(index, 1);
      saveRecipes(recipes);
      renderRecipes(recipes);
    });
    card.appendChild(removeBtn);

    recipesList.appendChild(card);

    // Aplicar animação
    setTimeout(() => {
      card.classList.add("show");
    }, 50 * index);
  });
}

// ----- Modal -----
addRecipeBtn.addEventListener("click", () => {
  recipeModal.classList.add("show");
});

closeModal.addEventListener("click", () => {
  recipeModal.classList.remove("show");
  setTimeout(() => {
    recipeModal.style.display = "none";
  }, 300);
});

// ----- Salvar receita -----
saveRecipeBtn.addEventListener("click", () => {
  const name = document.getElementById("recipe-name").value.trim();
  const ingredients = document.getElementById("recipe-ingredients").value.trim();
  const steps = document.getElementById("recipe-steps").value.trim();
  const category = categorySelect.value;
  const imageFile = document.getElementById("recipe-image").files[0];

  if (!name || !ingredients || !steps || !category) {
    alert("Preencha todos os campos e selecione uma categoria!");
    return;
  }

  const reader = new FileReader();
  reader.onload = function () {
    const imageData = reader.result;
    const recipes = loadRecipes();
    recipes.push({ name, ingredients, steps, image: imageData, category });
    saveRecipes(recipes);
    renderRecipes(recipes);
    recipeModal.classList.remove("show");
    setTimeout(() => recipeModal.style.display = "none", 300);

    // Resetar campos
    document.getElementById("recipe-name").value = "";
    document.getElementById("recipe-ingredients").value = "";
    document.getElementById("recipe-steps").value = "";
    categorySelect.value = "";
    document.getElementById("recipe-image").value = "";
  };

  if (imageFile) {
    reader.readAsDataURL(imageFile);
  } else {
    reader.onload();
  }
});

// ----- Buscar receitas -----
searchInput.addEventListener("input", () => {
  const query = searchInput.value.toLowerCase();
  const recipes = loadRecipes();
  const filtered = recipes.filter(
    r => r.name.toLowerCase().includes(query) || r.ingredients.toLowerCase().includes(query)
  );
  renderRecipes(filtered);
});

// ----- Filtros por categoria -----
filterBtns.forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelector(".filter-btn.active").classList.remove("active");
    btn.classList.add("active");

    const category = btn.getAttribute("data-category");
    const recipes = loadRecipes();
    const filtered = category === "all" ? recipes : recipes.filter(r => r.category === category);
    renderRecipes(filtered);
  });
});

// ----- Inicializar -----
document.addEventListener("DOMContentLoaded", () => {
  const recipes = loadRecipes();
  renderRecipes(recipes);
});

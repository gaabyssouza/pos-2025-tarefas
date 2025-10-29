import './style.css';
import { getPokemon, getPokemonList } from "./api/pokemonApi.js";

const pokemonListEl = document.querySelector("#pokemon-list");
const searchForm = document.querySelector("#search-form");
const searchInput = document.querySelector("#pokemon-name");


async function renderPokemon(name) {
  try {
    const pokemon = await getPokemon(name);
    pokemonListEl.innerHTML = `
      <div class="pokemon-card">
        <h3>${pokemon.name.toUpperCase()}</h3>
        <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}">
        <p>Altura: ${pokemon.height}</p>
        <p>Peso: ${pokemon.weight}</p>
      </div>
    `;
  } catch {
    pokemonListEl.innerHTML = "<p>Pokémon não encontrado 😢</p>";
  }
}


async function renderPokemonList() {
  const list = await getPokemonList(10);
  pokemonListEl.innerHTML = "";
  list.forEach(p => {
    const card = document.createElement("div");
    card.classList.add("pokemon-card");
    card.textContent = p.name;
    pokemonListEl.appendChild(card);
  });
}


searchForm.addEventListener("submit", e => {
  e.preventDefault();
  const name = searchInput.value.trim();
  if (name) renderPokemon(name);
});

renderPokemonList();

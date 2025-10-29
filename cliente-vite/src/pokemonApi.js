
const BASE_URL = "https://pokeapi.co/api/v2";

/**

 * @param {string|number} identifier - nome ou id do Pokémon
 */
export async function getPokemon(identifier) {
  try {
    const response = await fetch(`${BASE_URL}/pokemon/${identifier.toLowerCase()}`);
    if (!response.ok) throw new Error("Pokémon não encontrado!");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Erro na API:", error.message);
    throw error;
  }
}

/**
 * @param {number} limit 
 */
export async function getPokemonList(limit = 20) {
  try {
    const response = await fetch(`${BASE_URL}/pokemon?limit=${limit}`);
    const data = await response.json();
    return data.results;
  } catch (error) {
    console.error("Erro ao carregar lista:", error.message);
    throw error;
  }
}

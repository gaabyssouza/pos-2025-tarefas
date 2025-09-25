const pokemonList = document.getElementById('pokemon-list');
const pokemonDetails = document.getElementById('pokemon-details');

async function loadPokemonList() {
    const response = await fetch('https://pokeapi.co/api/v2/pokemon?limit=20');
    const data = await response.json();

    data.results.forEach(async (pokemon) => {
        const pokeData = await fetch(pokemon.url).then(res => res.json());

        const card = document.createElement('div');
        card.className = 'card';
        card.innerHTML = `
      <h3>${pokeData.name}</h3>
      <img src="${pokeData.sprites.front_default}" alt="${pokeData.name}" />
    `;
        card.addEventListener('click', () => showPokemonDetails(pokeData));
        pokemonList.appendChild(card);
    });
}

function showPokemonDetails(pokemon) {
    const types = pokemon.types.map(t => t.type.name).join(', ');
    const abilities = pokemon.abilities.map(a => a.ability.name).join(', ');
    const stats = pokemon.stats.map(s => `<li>${s.stat.name}: ${s.base_stat}</li>`).join('');

    pokemonDetails.classList.remove('hidden');
    pokemonDetails.innerHTML = `
    <h2>${pokemon.name}</h2>
    <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}" />
    <p><strong>Tipos:</strong> ${types}</p>
    <p><strong>Habilidades:</strong> ${abilities}</p>
    <p><strong>Altura:</strong> ${pokemon.height / 10} m</p>
    <p><strong>Peso:</strong> ${pokemon.weight / 10} kg</p>
    <h4>Estatísticas:</h4>
    <ul>${stats}</ul>`
        ;
}

loadPokemonList();

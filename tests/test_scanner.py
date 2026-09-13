from pokedex_scanner.catalog import PokemonRecord
from pokedex_scanner.scanner import identify, normalize


CATALOG = [
    PokemonRecord(25, "Pikachu", "Mouse Pokémon", ("Pikachuu",)),
    PokemonRecord(133, "Eevee", "Evolution Pokémon", ("Eievui",)),
]


def test_normalize() -> None:
    assert normalize(" Mouse-Pokémon! ") == "mouse pokemon"


def test_number_match_ranks_first() -> None:
    result = identify(["025", "Pikachu"], CATALOG)
    assert result.candidates[0].number == 25
    assert "pokedex-number" in result.candidates[0].evidence

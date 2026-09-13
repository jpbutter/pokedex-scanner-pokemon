import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PokemonRecord:
    number: int
    name: str
    category: str
    aliases: tuple[str, ...]


def load_catalog(path: Path) -> list[PokemonRecord]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [
        PokemonRecord(
            number=int(item["number"]),
            name=str(item["name"]),
            category=str(item["category"]),
            aliases=tuple(item.get("aliases", [])),
        )
        for item in payload
    ]


def default_catalog() -> list[PokemonRecord]:
    return load_catalog(Path(__file__).parents[2] / "data" / "pokemon.sample.json")

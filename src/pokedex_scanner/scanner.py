import re
import unicodedata
from difflib import SequenceMatcher

from .catalog import PokemonRecord
from .models import Candidate, IdentifyResponse


def normalize(value: str) -> str:
    ascii_value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", ascii_value.lower()).strip()


def _score(query: str, record: PokemonRecord) -> tuple[float, list[str]]:
    evidence: list[str] = []
    name_score = SequenceMatcher(None, query, normalize(record.name)).ratio()
    alias_score = max(
        (SequenceMatcher(None, query, normalize(alias)).ratio() for alias in record.aliases),
        default=0.0,
    )
    tokens = set(query.split())
    number_hit = str(record.number) in tokens or f"{record.number:03d}" in tokens
    if number_hit:
        evidence.append("pokedex-number")
    if name_score >= 0.55:
        evidence.append("name")
    if alias_score >= 0.55:
        evidence.append("alias")
    return round(max(name_score, alias_score, 0.98 if number_hit else 0.0), 4), evidence


def identify(tokens: list[str], catalog: list[PokemonRecord], limit: int = 3) -> IdentifyResponse:
    query = normalize(" ".join(tokens))
    candidates = []
    for record in catalog:
        confidence, evidence = _score(query, record)
        candidates.append(
            Candidate(
                number=record.number,
                name=record.name,
                category=record.category,
                confidence=confidence,
                evidence=evidence,
            )
        )
    candidates.sort(key=lambda candidate: candidate.confidence, reverse=True)
    return IdentifyResponse(normalized_query=query, candidates=candidates[:limit])

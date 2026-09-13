from fastapi import FastAPI

from . import __version__
from .catalog import default_catalog
from .models import IdentifyRequest, IdentifyResponse
from .scanner import identify

app = FastAPI(title="Pokédex Scanner Pokémon", version=__version__)
catalog = default_catalog()


@app.get("/health")
def health() -> dict[str, str | int]:
    return {"status": "ok", "version": __version__, "catalog_records": len(catalog)}


@app.post("/identify", response_model=IdentifyResponse)
def identify_endpoint(request: IdentifyRequest) -> IdentifyResponse:
    return identify(request.tokens, catalog, request.limit)

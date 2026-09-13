from pydantic import BaseModel, Field


class IdentifyRequest(BaseModel):
    tokens: list[str] = Field(min_length=1, max_length=30)
    limit: int = Field(default=3, ge=1, le=10)


class Candidate(BaseModel):
    number: int
    name: str
    category: str
    confidence: float
    evidence: list[str]


class IdentifyResponse(BaseModel):
    normalized_query: str
    candidates: list[Candidate]

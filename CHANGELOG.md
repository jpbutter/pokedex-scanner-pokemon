# Changelog

This project follows Semantic Versioning.

## [0.1.0] - 2026-09-13

### Added

- FastAPI health and identification endpoints
- Unicode-aware observation normalization
- Ranked matching by name, aliases and Pokédex number
- Small demonstration catalog with synthetic request data
- Unit tests, CI, architecture notes and security guidance

### Known limitations

Version 0.1 accepts text observations rather than images. Confidence values describe string similarity and are not calibrated probabilities.
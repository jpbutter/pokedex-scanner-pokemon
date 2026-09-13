# API

## GET /health

Returns service status, semantic version and the number of loaded catalog records.

## POST /identify

Request fields:

- **tokens:** one to thirty OCR-style text observations
- **limit:** maximum candidates, from one to ten

The response contains the normalized query and ranked candidates. Confidence is a matching score, not an identification guarantee.

Run the app with **uvicorn pokedex_scanner.api:app --reload** and inspect the generated OpenAPI page under **/docs**.
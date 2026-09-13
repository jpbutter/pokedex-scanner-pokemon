# Architecture

The prototype uses replaceable pipeline stages.

## Acquisition

A future adapter receives a camera frame or upload and owns orientation, size limits and privacy-safe temporary handling. Version 0.1 intentionally accepts no images.

## Observation extraction

An OCR or vision component converts pixels into small observations such as a name, number or category. The core matcher is vendor-independent.

## Normalization and ranking

Case, punctuation and common Unicode differences are normalized. Catalog records are scored using deterministic text similarity and a strong number match. The result is explainable but not a calibrated probability.

## Confirmation

Clients should display candidates and let the user confirm them. A later release will return unknown when evidence is weak.

## Trust boundary

Camera frames and OCR output may contain personal information. They must be isolated from public catalog data and should not be retained by default.
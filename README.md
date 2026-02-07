# Optimisation Traige Pipeline

A reproducible, data-driven framework for screening and ranking several structural components to identify high-value candidates for optimisation before running computationally expensive optimisation solvers.

The pipeline aims to ingest structural metadata (e.g. mass distribution, load utilisation, design variables), engineers interpretable features and applies deterministics scoring and ranking logic to answer a single question:

Which parts are worth optimising (or atleast should be prioritised)

This project explicitly seperates triage from optimisation to:
- Reduce solver cost and engineering effort
- Audit and certify decision logic
- Scale and pre-process for downstream optimisation or ML workflows

# Confidential Data Guardrails

- Treat all files under `datasets-dashboard/` as confidential and out-of-scope.
- Do not open, read, parse, summarize, or quote anything from `datasets-dashboard/**`.
- Do not use `rg`, `grep`, `cat`, `head`, `tail`, or similar commands against `datasets-dashboard/**`.
- Use only synthetic/demo values already present in UI files or explicitly created dummy data.
- If a task would require confidential data, stop and propose a mock-data alternative.

# Demo Data Policy

- Keep prototypes runnable using local synthetic data only.
- Prefer deterministic dummy data for usability tests and screenshots.
- Mark generated values as fictional in documentation.
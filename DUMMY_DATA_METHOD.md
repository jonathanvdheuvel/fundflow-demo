# Dummy Data Method (FundFlow)

Date: 17 March 2026

## Short answer

The live prototype does not read or load real dataset files at runtime.

Confidential files from datasets-dashboard were not uploaded or submitted to an AI tool as part of this prototype publication flow.

## What was changed

1. A single in-page object named SYNTHETIC_DATA was added in fundflow.html.
2. The three UI tables are rendered from SYNTHETIC_DATA:
   - Reports table
   - Contracts table
   - Error table
3. KPI cards are calculated from SYNTHETIC_DATA using updateKpisFromSyntheticData.
4. Synthetic rendering and KPI updates run on page load through initializeSyntheticData.

## How dummy values were created

1. Data was authored manually as fictional records.
2. Values were made realistic for UX testing (budget amounts, statuses, dates, approval differences).
3. Records were deterministic (fixed values in code) so screenshots and usability tests remain reproducible.

## Confidentiality controls

1. datasets-dashboard is marked confidential and out-of-scope in .github/copilot-instructions.md.
2. datasets-dashboard is excluded from git tracking via .gitignore.
3. Public hosting uses only checked-in demo files; confidential datasets are not published.
4. Synthetic values are authored directly in fundflow.html as fixed fictional records.

## Verification summary

- No runtime fetch or API call is used for data loading in fundflow.html.
- No CSV or JSON file is loaded by runtime code.
- Runtime data references point to SYNTHETIC_DATA only.

## Re-check command

Run this in the project root to re-audit references:

rg -n "datasets-dashboard|fetch\(|XMLHttpRequest|axios|d3\.csv|read_csv|\.csv|\.json|SYNTHETIC_DATA|renderSynthetic|updateKpisFromSyntheticData" --glob '!datasets-dashboard/**' fundflow.html README.md serve.py .github/copilot-instructions.md

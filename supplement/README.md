# Reproducibility and Review Supplement for PACE

This supplement accompanies the manuscript and is synchronized to the 15-item positively keyed survey specification (where Item 13 is `PERSUASIVENESS` and the secondary AI Agreement Index, AAI, averages all 15 items with equal item weight $1/15$).

## Contents

- **S1 `INSTRUMENT_VI.md`:** All 15 Vietnamese statements, English translations, conceptual groupings (Table 1), regression predictor/outcome mappings (Eq. 1 / Table 3), and historical export column mapping.
- **S2 `PROCEDURE_UI.md`:** Batch 4-answer submission workflow prior to viewing feedback, random configuration permutation vs. submission-order survey navigation, student-blinded rendering (`ui_source/`), and research ethics / repository governance disclosures.
- **S3 `aggregate/cluster_sufficient_statistics.json` & `scripts/reproduce.py`:** Standalone NumPy reproduction script reconstructing RQ1 item means/CIs, RQ2 15-item AAI paired contrasts and 90-contrast simultaneous sensitivity bands, and RQ3 context models from 28-repository sufficient statistics without exposing student identifiers or response text. Outputs `aggregate/additional_results.json`.
- **S4 `CONFIGURATION_PROFILES.md`:** Configuration means and repository-bootstrap intervals.
- **S5 `PROMPTS_AND_SCHEMAS.md`:** Verbatim study-version system/user prompts, XML delimiter sandboxing tags, JSON schemas for all four configurations, Stage 1 & Stage 2 `Researching` prompts, single-model fallback behavior, and model provenance notes separating study-window commit `a2f61f0` from post-collection commits.
- **S6 `FEEDBACK_EXAMPLES_DEIDENTIFIED.md`:** Four de-identified authentic AI feedback JSON payloads (`Sandwich`, `Rubric`, `Explainable`, `Researching`) from the study dataset.
- **`tables/EXPLORATORY_RESULTS.md`:** Complete 90-contrast item comparison family and RQ3 context models.
- **`original_pipeline/`:** Synchronized manuscript (`main.tex`), figures (`figures/likert_items.pdf`), LaTeX tables (`analysis/tables/*.tex`), and analysis scripts.

## Run Without Private Records

```bash
python3 -m pip install -r requirements-minimal.txt
python3 scripts/reproduce.py
```

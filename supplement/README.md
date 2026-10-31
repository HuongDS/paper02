# Reproducibility and Review Supplement for PACE

This supplement accompanies the manuscript *"Do Students Agree with LLM Feedback on Their Own Code? A Within-Subject Study of Four Feedback Configurations in Software Project Courses"* and is 100% synchronized with the 15-item positively keyed survey instrument (where Criterion 13 is `PERSUASIVENESS` and the secondary AI Agreement Index, AAI, averages all 15 items with equal item weight $1/15$).

## Key Synchronized Metrics Summary

- **Sample Structure:** 344 complete feedback-rating instances from 86 students across 28 project repositories ($k = 4$ scenario answers submitted as a single batch per student before viewing any feedback; 86 instances per assigned configuration: `Sandwich`, `Rubric`, `Explainable`, `Researching`; 280 `Graph` and 64 `Raw` instances).
- **Instrument Provenance (Oct 20–26 Collection vs. Oct 31 Metadata Reconciliation):** All 15 positively keyed Vietnamese statements (including Criterion 13 on argument persuasiveness) were displayed verbatim to students in `step-survey-rubric.tsx` throughout the October 20–26, 2026 collection window and were not modified during or after the study. The October 31 criterion specification (`PACE_Tieu_Chi_Khao_Sat_2026-10-31.xlsx`) only reconciled the English metadata label for Criterion 13 (`PERSUASIVENESS`, replacing a legacy `(REJECTION)` column header tag in the raw export template).
- **Primary & Key Item Outcomes (RQ1):**
  - `ACCEPTANCE` (direct agreement with AI judgment): Mean $4.09$ (SD $0.82$), 95% repository-bootstrap CI $[3.90, 4.27]$, $79.9\%$ agree ($\ge 4$), $3.5\%$ disagree ($\le 2$).
  - `PERSUASIVENESS` (conviction in AI arguments/evidence): Mean $2.87$ (SD $1.22$), 95% CI $[2.56, 3.20]$, $30.8\%$ agree, $48.8\%$ disagree.
  - `AFFECT` (learning motivation): Mean $3.53$ (SD $0.87$), 95% CI $[3.38, 3.71]$, $41.9\%$ agree ($53.2\%$ neutral, $4.9\%$ disagree).
  - `BEHAVIORAL INTENTION` (future-use intention): Mean $3.80$ (SD $0.85$), 95% CI $[3.65, 3.94]$, $68.0\%$ agree, $5.2\%$ disagree.
  - **15-item unweighted AAI:** Mean $3.99$ (SD $0.60$), 95% repository-bootstrap CI $[3.85, 4.13]$.
- **Pooled Internal Consistency (§5.1):**
  - 15-item AAI pooled across 344 instances: Cronbach's $\alpha = 0.916$ ($0.9158$), one-factor McDonald's $\omega_t = 0.930$ ($0.9304$).
  - Excluding 64 straight-lined instances ($n = 280$ non-straight-lined instances): 15-item pooled $\alpha = 0.868$ ($\approx 0.87$).
  - Predictor composites (Eq. 1 / Table 3): `Perceived Quality (PQ)` (4 items: `ACCURACY`, `SPECIFICITY`, `CLARITY`, `TRANSPARENCY`) $\alpha = 0.905$ ($0.904875$); `Perceived Utility (PU)` (2 items: `USEFULNESS`, `ACTIONABILITY`) $\alpha = 0.783$; `Trust & Fairness (TR)` (3 items: `COMPETENCE TRUST`, `RELIABILITY`, `FAIRNESS`) $\alpha = 0.796$; three outcome items (`ACCEPTANCE`, `WILLINGNESS`, `BEHAVIORAL INTENTION`) $\alpha = 0.780$; two-item `Affect & Safety` pair (`AFFECT`, `PSYCHOLOGICAL SAFETY`) $\alpha = 0.561$ (entered as separate single-item predictors in Eq. 1).
- **Configuration Comparisons (RQ2):**
  - All 6 paired 95% repository-bootstrap CIs on `ACCEPTANCE` include zero.
  - 15-item AAI means by assigned configuration: `Sandwich` $4.04$, `Researching` $4.01$, `Explainable` $3.99$, `Rubric` $3.93$.
  - Exploratory Friedman test on 15-item AAI: $\chi^2(3) = 25.44$ ($p < .001$, Kendall's $W = 0.099$); omnibus student-intercept mixed-effects model $p = 0.071$.
  - 90% repository-bootstrap CI-inclusion check on 15-item AAI: 6/6 pairs within $\pm 0.25$, 5/6 within $\pm 0.20$, 1/6 within $\pm 0.10$.
- **Observational Context Comparison (RQ3):**
  - `ACCEPTANCE`: `Graph` ($n=280$) $4.06$ vs. `Raw` ($n=64$) $4.20$; adjusted $b_{\text{raw}} = 0.034$, 95% CI $[-0.180, 0.257]$.
  - 15-item `AAI`: `Graph` $3.98$ vs. `Raw` $4.04$; adjusted $b_{\text{raw}} = 0.074$, 95% CI $[-0.020, 0.190]$.

## Contents Mapped to Manuscript Sections S1–S6

- **S1 `INSTRUMENT_VI.md`:** Verbatim 15 Vietnamese statements shown during October 20–26 data collection, English translations, conceptual groupings (Table 1), regression predictor/outcome mappings (Eq. 1 / Table 3), and October 31 metadata header reconciliation note.
- **S2 `PROCEDURE_UI.md`:** Batch 4-answer submission workflow prior to viewing feedback, backend random configuration permutation (`Random.Shared.Shuffle`) vs. submission-order survey navigation, student-blinded rendering (`ui_source/`), and research ethics / repository governance disclosures.
- **S3 `PROMPTS_AND_SCHEMAS.md`:** Verbatim study-version system/user prompts, XML delimiter tags, JSON schemas for all four configurations, Stage 1 & Stage 2 `Researching` prompts, single-model fallback behavior (`models_involved` schema template provenance), and model provenance separating study-window commit `a2f61f0` from post-collection commits.
- **S4 `FEEDBACK_EXAMPLES_DEIDENTIFIED.md`:** Four de-identified authentic AI feedback JSON payloads (`Sandwich`, `Rubric`, `Explainable`, `Researching`) from the study dataset, with student-facing rendered views and 15-item rating vectors.
- **S5 `CONFIGURATION_PROFILES.md`:** Assigned configuration profiles, means, and repository-bootstrap intervals.
- **S6 `tables/EXPLORATORY_RESULTS.md`, `aggregate/`, & `scripts/reproduce.py`:** Complete 90-contrast item comparison family, RQ2 15-item AAI contrasts, RQ3 context models, and standalone NumPy reproduction script (`scripts/reproduce.py`) reconstructing results from 28-repository sufficient statistics (`aggregate/cluster_sufficient_statistics.json`) into `aggregate/additional_results.json`.
- **`original_pipeline/`:** Synchronized manuscript (`main.tex`), vector figures (`figures/likert_items.pdf`, `figures/format_constructs.pdf`), LaTeX tables (`analysis/tables/*.tex`), and synchronized analysis outputs (`analysis/results.json`, `analysis/source_audit.json`, `analysis/leave_one_repository_out.json`).

## Run Without Private Records

```bash
python3 -m pip install -r requirements-minimal.txt
python3 scripts/reproduce.py
```

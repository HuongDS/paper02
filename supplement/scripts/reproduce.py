#!/usr/bin/env python3
"""Reproduce RQ1 item summaries, RQ2 15-item AAI contrasts, 90-contrast multiplicity bands, and RQ3 models from cluster aggregates."""
import itertools, json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
FORMATS = ['Sandwich', 'Rubric', 'Explainable', 'Researching']

def main():
    s = json.loads((ROOT / 'aggregate/cluster_sufficient_statistics.json').read_text(encoding='utf-8'))
    # 1. Seed 20261030 common-draw multiplicity family (90 item contrasts) & RQ3 context models
    rng = np.random.default_rng(s['seed'])
    k = s['repository_count']
    b = s['replicates']
    weights = rng.multinomial(k, np.full(k, 1 / k), size=b)
    counts = np.array(s['cluster_student_counts'], dtype=float)
    totals = np.array(s['contrast_cluster_sums'], dtype=float)
    point = totals.sum(axis=0) / counts.sum()
    boot = weights @ totals / (weights @ counts)[:, None]
    se = boot.std(axis=0, ddof=1)
    if (se <= 0).any():
        raise ValueError('Zero bootstrap SD in comparison family')
    maximum = np.max(np.abs((boot - point) / se), axis=1)
    cut = float(np.quantile(maximum, 0.95))
    contrasts = []
    for j, label in enumerate(s['contrast_labels']):
        contrasts.append({
            **label,
            'difference': float(point[j]),
            'ci95_unadjusted': np.quantile(boot[:, j], [0.025, 0.975]).tolist(),
            'ci95_simultaneous_90_comparisons': [float(point[j] - cut * se[j]), float(point[j] + cut * se[j])],
            'max_stat_adjusted_tail_fraction': float((1 + np.sum(maximum >= abs(point[j] / se[j]))) / (b + 1))
        })

    xtx = np.array([m['xtx'] for m in s['context_cluster_moments']], dtype=float)
    xty = np.array([m['xty'] for m in s['context_cluster_moments']], dtype=float)
    matrices = np.einsum('br,rij->bij', weights, xtx)
    responses = np.einsum('br,rij->bij', weights, xty)
    if not np.all(np.linalg.matrix_rank(matrices) == len(s['context_predictors'])):
        raise ValueError('Rank deficient bootstrap context model')
    coeff = np.linalg.solve(xtx.sum(axis=0), xty.sum(axis=0))
    draws = np.linalg.solve(matrices, responses)
    context = {
        'ACCEPTANCE': {
            'b_raw': float(coeff[0, 0]),
            'ci95_repository': np.quantile(draws[:, 0, 0], [0.025, 0.975]).tolist(),
            'valid_fits': b
        },
        'AAI': s.get('context_aai15_summary', {
            'b_raw': float(coeff[0, 1]),
            'ci95_repository': np.quantile(draws[:, 0, 1], [0.025, 0.975]).tolist(),
            'valid_fits': b
        })
    }

    # 2. Seed 20261029 repository bootstrap for RQ1 item CIs, 15-item AAI overall CI, and 6 paired 15-item AAI contrasts
    rng29 = np.random.default_rng(20261029)
    sampled29 = rng29.integers(0, k, (b, k))
    rating_counts = np.array(s['cluster_item_rating_counts'], dtype=float)
    rating_sums = rating_counts @ np.arange(1, 6, dtype=float)
    rating_n = rating_counts.sum(axis=2)

    item_boot = weights @ rating_sums / (weights @ rating_n)
    item_summary = {}
    for j, item in enumerate(s['item_labels']):
        boots29 = rating_sums[:, j][sampled29].sum(axis=1) / rating_n[:, j][sampled29].sum(axis=1)
        item_summary[item] = {
            'mean': float(rating_sums[:, j].sum() / rating_n[:, j].sum()),
            'agree_percent': float(100 * rating_counts[:, j, 3:].sum() / rating_n[:, j].sum()),
            'disagree_percent': float(100 * rating_counts[:, j, :2].sum() / rating_n[:, j].sum()),
            'ci95_repository_seed20261029': np.percentile(boots29, [2.5, 97.5]).tolist(),
            'ci95_repository_new_seed': np.quantile(item_boot[:, j], [0.025, 0.975]).tolist()
        }

    aai15_cluster_sums = rating_sums.mean(axis=1)
    aai15_cluster_ns = rating_n[:, 0]
    aai15_boots29 = aai15_cluster_sums[sampled29].sum(axis=1) / aai15_cluster_ns[sampled29].sum(axis=1)
    aai15_overall = {
        'mean': float(aai15_cluster_sums.sum() / aai15_cluster_ns.sum()),
        'ci95_repository_seed20261029': np.percentile(aai15_boots29, [2.5, 97.5]).tolist()
    }

    aai15_pairs = []
    for fa, fb in itertools.combinations(FORMATS, 2):
        idxs = [j for j, lbl in enumerate(s['contrast_labels']) if lbl['a'] == fa and lbl['b'] == fb]
        pair_totals = totals[:, idxs].mean(axis=1)
        md = float(pair_totals.sum() / counts.sum())
        p_boots = pair_totals[sampled29].sum(axis=1) / counts[sampled29].sum(axis=1)
        ci90 = np.percentile(p_boots, [5.0, 95.0]).tolist()
        ci95 = np.percentile(p_boots, [2.5, 97.5]).tolist()
        aai15_pairs.append({
            'a': fa, 'b': fb,
            'mean_difference': md,
            'ci90_repository': ci90,
            'ci95_repository': ci95,
            'within_margin_025': bool(ci90[0] >= -0.25 and ci90[1] <= 0.25),
            'within_margin_020': bool(ci90[0] >= -0.20 and ci90[1] <= 0.20),
            'within_margin_010': bool(ci90[0] >= -0.10 and ci90[1] <= 0.10)
        })

    result = {
        'aai15_overall': aai15_overall,
        'aai15_pairs': aai15_pairs,
        'item_summary': item_summary,
        'replicates': b,
        'seed': s['seed'],
        'multiplicity_family': '15 items x 6 configuration pairs = 90 two-sided contrasts (15 positively keyed items including PERSUASIVENESS)',
        'simultaneous_method': '95% centred bootstrap-standardised maximum band; fixed bootstrap SD per contrast, not nested studentisation; exploratory approximate sensitivity',
        'max_stat_critical_value': cut,
        'context': context,
        'contrasts': contrasts
    }
    (ROOT / 'aggregate/additional_results.json').write_text(json.dumps(result, indent=2, allow_nan=False) + '\n', encoding='utf-8')
    chosen = next(c for c in contrasts if c['item'] == 'ACTIONABILITY' and c['a'] == 'Sandwich' and c['b'] == 'Explainable')
    print(json.dumps({'aai15_overall': aai15_overall, 'context': context, 'actionability_Sandwich_Explainable': chosen}, indent=2))

if __name__ == '__main__':
    main()

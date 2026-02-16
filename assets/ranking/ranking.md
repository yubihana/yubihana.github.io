# White Paper: A Ranking System for Press-On Nails

**Version:** 1.0  
**Date:** February 14, 2026  
**Purpose:** Define a transparent, repeatable, and quantitative ranking framework for press-on nails across material quality and value, craftsmanship, beauty design quality, adhesion performance, safety standards, and total value proposition.

---

## Executive Summary

Press-on nails have moved from a niche beauty accessory to a mainstream at-home beauty category. To support consumers, retailers, and brands, this paper proposes a standardized ranking model that:

1. Uses six weighted dimensions with clear scoring criteria.
2. Separates hard-gate safety requirements from performance scoring.
3. Combines lab testing, expert review, and user wear trials.
4. Produces a final score, tier ranking, and confidence score.
5. Supports quarterly updates as market and regulations evolve.

This model is designed to be practical for 2026 operations while scalable for future AI-assisted and sustainability-aware benchmarking.

---

## 1) 2026 Market Context

Publicly available 2026 market signals indicate continued growth and strong consumer demand for DIY nail solutions:

- Grand View Research reports the global press-on nails market at **USD 738.0M in 2024**, with **USD 1,075.0M projected by 2030** at **6.5% CAGR (2025-2030)**.
- Using that CAGR path as an approximation, the implied 2026 market level is about **USD 0.84B** (inference: `738.0 * 1.065^2`).
- Fortune Business Insights reports the global artificial nails market at **USD 1.68B in 2026**, with the **press-on segment share at 33.93% in 2026** (implied press-on segment ~**USD 0.57B** within that dataset).

These figures suggest a large enough category to justify a formal ranking system with standardized quality and safety signals.

---

## 2) Regulatory and Safety Baseline

### 2.1 ISO 22716 (Cosmetics GMP)

ISO 22716:2007 provides guidelines for production, control, storage, and shipment of cosmetic products and remains current after review confirmation in 2022.  
For ranking eligibility, manufacturers should provide one of:

- Valid ISO 22716 certification, or
- Equivalent audited GMP documentation.

### 2.2 REACH and EU Chemical Restrictions

REACH (Regulation (EC) No 1907/2006) sets EU-wide rules on registration, evaluation, authorization, and restriction of chemicals, including Annex XVII restrictions.

Additionally, Commission Regulation (EU) 2023/2055 introduced microplastics restrictions with transitional dates relevant to cosmetics, including:

- Rinse-off cosmetics: until October 16, 2027
- Leave-on cosmetics: until October 16, 2029
- Make-up, lip, and nail cosmetics: until October 16, 2035 (with specific labeling requirements from October 17, 2031 to October 16, 2035)

### 2.3 Safety Gating Rule (Pass/Fail)

A product is not rank-eligible unless it passes all safety gates:

1. Ingredient disclosure completeness for nail tips and adhesive (or adhesive tabs).
2. Evidence of compliance with target-market chemical restrictions (for example, REACH-relevant restricted substances declarations for EU claims).
3. Manufacturing quality evidence (ISO 22716 certificate or equivalent GMP evidence).
4. No unresolved serious safety alerts, recalls, or documented contamination events.

If a product fails any gate, it is marked **Not Ranked - Safety Non-Compliance**.

---

## 3) Ranking Framework Overview

### 3.1 Dimensions and Weights

| Dimension | Weight | Why it matters |
|---|---:|---|
| Material Quality and Functional Value | 22% | Durability, comfort, realism, and reusability start with material performance. |
| Craftsmanship | 18% | Precision fit, edge finishing, consistency, and defect control drive user trust. |
| Design and Beauty Aesthetic Quality | 18% | Style quality, trend relevance, and visual execution influence purchase and satisfaction. |
| Adhesion Performance | 17% | Wear duration and failure rate are core to real-world utility. |
| Safety Standards and Compliance | 20% | Chemical and process safety are non-negotiable foundations. |
| Value Proposition (Based on All Above) | 5% | Evaluates total user value relative to price per effective wear. |

Total weight = 100%.

### 3.2 Scoring Scale

Each dimension is scored 0-100 from defined sub-metrics.  
Overall score:

`Overall = Sum(DimensionScore_i * Weight_i) / 100`

Score is reported with one decimal place.

### 3.3 Confidence Score

To prevent overconfident rankings with limited data:

`Confidence = DataCoverage * MethodReliability`

- `DataCoverage` (0.70-1.00): how complete the required dataset is.
- `MethodReliability` (0.80-1.00): inter-rater consistency + repeat-test consistency.

Publish both `Overall Score` and `Confidence Score`.

---

## 4) Quantitative Methodology by Dimension

### 4.1 Material Quality and Functional Value (28%)

Sub-metrics:

- Tip material integrity (bend/flex resistance, cracking under standardized stress)
- Thickness consistency (coefficient of variation across sampled nails)
- Surface durability (scratch and gloss retention after wear simulation)
- Comfort and natural feel (panel score)
- Reusability performance (condition after controlled removal and reapplication)

Suggested scoring bands:

- 90-100: High integrity, low variance, strong reusability, premium comfort
- 75-89: Solid quality with minor variance
- 60-74: Acceptable but inconsistent or less durable
- <60: Frequent defects or poor durability

### 4.2 Craftsmanship (28%)

Sub-metrics:

- Shape symmetry and dimensional precision across sizes
- Cuticle-edge finish quality
- Paint/print/coating consistency
- Defect rate (bubbles, chips, rough edges, misaligned designs)
- Size set completeness and fit grading quality

Measurement examples:

- Dimensional tolerance checks using calipers
- Defects per 100 nails sampled
- Expert panel blind review

### 4.3 Design and Beauty Aesthetic Quality (18%)

Sub-metrics:

- Visual harmony (color, proportion, line precision)
- Trend relevance (quarterly trend rubric for 2026)
- Finish quality (gloss, matte, chrome, texture control)
- Distinctiveness and collection coherence
- User appeal rating from target cohorts

Method:

- Blind aesthetic panel (expert + consumer mix)
- 5-point rubric mapped to 0-100 scale

### 4.4 Adhesion Performance (18%)

Sub-metrics:

- Median wear duration in days under standardized daily-use protocol
- Early failure rate at 24h and 72h
- Full-set retention curve at day 3, day 5, day 7
- Water/household-activity resilience
- Removal damage incidence (nail plate stress proxy and user discomfort report)

Minimum test protocol:

- At least 30 participants across common nail types
- Separate runs for glue and adhesive-tab usage
- Report environment and user behavior controls

### 4.5 Safety Standards and Compliance (8%)

Sub-metrics:

- Documentation completeness (INCI, SDS where applicable, claims substantiation)
- Restricted-substance compliance evidence
- Manufacturing quality evidence (ISO 22716 or equivalent GMP records)
- Packaging and labeling clarity (warnings, directions, allergy precautions)
- Post-market safety signal handling maturity

This dimension does not replace the hard safety gate. It differentiates strong vs minimal compliance among gate-passing products.

---


## 5) Final Ranking Output

### 5.1 Tier Labels

| Final Score | Tier | Interpretation |
|---:|---|---|
| 90.0-100 | Platinum | Best-in-class across performance, safety, and value |
| 80.0-89.9 | Gold | Strong, reliable performance with minor trade-offs |
| 70.0-79.9 | Silver | Good but notable limitations in one or more dimensions |
| 60.0-69.9 | Bronze | Basic acceptable performance; improvement needed |
| <60.0 | Watchlist | Below expected quality threshold |

All published rankings should include:

- Overall score
- Dimension-level scores
- Confidence score
- Safety gate status
- Test date and protocol version

---

## References (Primary and Market Sources)

1. ISO. ISO 22716:2007 Cosmetics - Good Manufacturing Practices (GMP).  
   https://www.iso.org/standard/36437.html

2. EUR-Lex. Regulation (EC) No 1907/2006 (REACH), consolidated text (current versions).  
   https://eur-lex.europa.eu/eli/reg/2006/1907/2020-02-27

3. European Commission. Commission Regulation (EU) 2023/2055 - microplastics restriction implementation details and transitional periods.  
   https://single-market-economy.ec.europa.eu/sectors/chemicals/reach/restrictions/commission-regulation-eu-20232055-restriction-microplastics-intentionally-added-products_en

4. Grand View Research. Press-on Nails Market Size, Share and Trends Report, 2030 (summary data used for 2024 base and CAGR assumptions).  
   https://www.grandviewresearch.com/industry-analysis/press-on-nails-market-report

5. Fortune Business Insights. Artificial Nails Market Size, Share, Trends, Global Report [2034] (2026 estimated year values and segment shares).  
   https://www.fortunebusinessinsights.com/artificial-nails-market-110177

### Notes on Inference

- The 2026 press-on market figure derived from Grand View Research is an interpolation based on published 2024 base value and 2025-2030 CAGR and should be treated as an analytical estimate, not a directly reported figure.

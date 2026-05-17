
# Project Cycle 3: Two-Sample Inference

## Group Information
- **Group Number:** 13
- **Member Names:** 113370219 謝紫旋, 113370232 周以心

---

## Dataset Used
YRBS_2007.csv

---

## Selected Variables
- **Group variable:** WhatIsYourSex
- **Response variable:** CurrentAlcoholUse

---

## Benchmark Values
- Sample size (Male): 6,425
- Sample size (Female): 6,234
- Proportion of current drinkers (Male): 0.5273 (52.73%)
- Proportion of current drinkers (Female): 0.5012 (50.12%)
- Difference (Male − Female): 0.0261

---

## Short Project Questions

### Proportion Analysis
Is there a significant difference in the proportion of current alcohol use between male and female students?

### Mean Analysis


---

## Project Workflow
1. Loaded and cleaned `YRBS_2007_cleaned.csv`
2. Recoded `CurrentAlcoholUse`: 1 → 0 (non-drinker), 2–7 → 1 (current drinker)
3. Recoded `WhatIsYourSex`: 1 → Male, 2 → Female
4. Computed descriptive statistics (proportions) by group
5. Stated hypotheses: H₀: p_male − p_female = 0 vs H₁: p_male − p_female ≠ 0 (α = 0.05)
6. Conducted Two-Proportion Z-Test
7. Computed 95% Confidence Interval for the difference in proportions
8. Visualized results with bar chart and CI plot

---

## Short Final Conclusions

### Proportion Analysis
Based on the YRBS 2007 data, 52.73% of male students and 50.12% of female students reported current alcohol use. Although males showed a slightly higher proportion, the Two-Proportion Z-Test resulted in Z = −1.3442 and p-value = 0.1789, which is greater than α = 0.05. Therefore, we fail to reject H₀ and conclude that there is no statistically significant difference in current alcohol use between male and female students.

### Mean Analysis


---

## Project Files
- `notebook/03_descriptive_statistics.ipynb`
- `notebook/04_two-sample_inference.ipynb`
- `data/Processed/YRBS_2007_cleaned.csv`
- `outputs/figures/bar_alcohol_by_sex.png`
- `outputs/figures/inference_alcohol_by_sex.png`
- `outputs/tables/descriptive_summary_alcohol_by_sex.csv`
- `outputs/tables/inference_alcohol_by_sex.csv`


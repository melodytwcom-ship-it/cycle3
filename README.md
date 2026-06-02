# Project Cycle 3: Two-Sample Inference
#project Repository:
https://github.com/melodytwcom-ship-it/project-cycle-3/blob/main/README.md

#Presentation video:
https://drive.google.com/file/d/1hmlH77GjDpxa5hvt1Zf1vQ10skXWISBE/view?usp=drivesdk

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

### Proportion Analysis
- Sample size (Male): 6,425
- Sample size (Female): 6,234
- Proportion of current drinkers (Male): 0.5273 (52.73%)
- Proportion of current drinkers (Female): 0.5012 (50.12%)
- Difference (Male − Female): 0.0261

### Mean Analysis
- Sample size (Male): 6,425
- Sample size (Female): 6,234
- Mean CurrentAlcoholUse (Male): 1.8139
- Mean CurrentAlcoholUse (Female): 1.9966
- Difference (Male − Female): −0.1827

---

## Short Project Questions

### Proportion Analysis
Is there a significant difference in the **proportion** of current alcohol use between male and female students?

### Mean Analysis
Is there a significant difference in the **mean alcohol use frequency** between male and female students?

---

## Project Workflow
1. Loaded and cleaned `YRBS_2007_cleaned.csv`
2. Recoded `WhatIsYourSex`: 1 → Male, 2 → Female
3. **Proportion Analysis:**
   - Recoded `CurrentAlcoholUse`: 1 → 0 (non-drinker), 2–7 → 1 (current drinker)
   - Computed proportions by group
   - Conducted Two-Proportion Z-Test
   - Computed 95% Confidence Interval for difference in proportions
4. **Mean Analysis:**
   - Used raw `CurrentAlcoholUse` scores (1–7) as continuous variable
   - Computed descriptive statistics (mean, std, median) by group
   - Conducted Welch's Two-Sample T-Test
   - Computed 95% Confidence Interval for difference in means
5. Visualized results with bar charts and CI plots

---

## Short Final Conclusions

### Proportion Analysis
Based on the YRBS 2007 data, 52.73% of male students and 50.12% of female students reported current alcohol use. Although males showed a slightly higher proportion, the Two-Proportion Z-Test resulted in Z = −1.3442 and p-value = 0.1789, which is greater than α = 0.05. Therefore, we fail to reject H₀ and conclude that there is no statistically significant difference in the proportion of current alcohol use between male and female students.

### Mean Analysis
Based on the YRBS 2007 data, male students had a mean alcohol use frequency score of 1.8139, while female students had a mean of 1.9966, indicating females reported slightly higher frequency. The Welch's Two-Sample T-Test resulted in T = −7.9389 and p-value < 0.0001, which is less than α = 0.05. Therefore, we reject H₀ and conclude that there is a statistically significant difference in mean alcohol use frequency between male and female students, with females reporting higher frequency on average.

---

## Project Files
- `notebook/03_descriptive_statistics.ipynb`
- `notebook/04_two-sample_inference.ipynb`
- `notebook/05_mean_inference.ipynb`
- `data/Processed/YRBS_2007_cleaned.csv`
- `outputs/figures/bar_alcohol_by_sex.png`
- `outputs/figures/inference_alcohol_by_sex.png`
- `outputs/figures/mean_inference_alcohol_by_sex.png`
- `outputs/tables/descriptive_summary_alcohol_by_sex.csv`
- `outputs/tables/inference_alcohol_by_sex.csv`
- `outputs/tables/mean_inference_alcohol_by_sex.csv`

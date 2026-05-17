# Summary Interpretation

## Overview

This project investigates whether gender is associated with alcohol use among high school students using data from the Youth Risk Behavior Surveillance System (YRBS) 2007. Two complementary analyses were conducted on the same variables (`WhatIsYourSex` and `CurrentAlcoholUse`): a proportion analysis examining whether students currently drink, and a mean analysis examining how frequently they drink.

---

## Analysis 1: Proportion Analysis (Two-Proportion Z-Test)

### What We Tested
Whether the proportion of students who reported current alcohol use differed between male and female students.

`CurrentAlcoholUse` was recoded as binary:
- **0** = non-drinker (original code 1: 0 days in past 30 days)
- **1** = current drinker (original codes 2–7: ≥1 day in past 30 days)

### Results

| | Male | Female |
|---|---|---|
| Sample size (n) | 6,425 | 6,234 |
| Current drinkers | 52.73% | 50.12% |
| Difference (Male − Female) | −0.0119 | |
| Z-statistic | −1.3442 | |
| P-value | 0.1789 | |
| 95% CI for difference | (−0.0292, 0.0054) | |

### Interpretation
Although male students showed a slightly higher proportion of current alcohol use (52.73%) compared to female students (50.12%), the difference of −0.0119 was not statistically significant (Z = −1.3442, p = 0.1789 > 0.05). We therefore **fail to reject H₀** and conclude that there is insufficient evidence to suggest a significant difference in the proportion of current alcohol use between male and female students.

The 95% confidence interval for the difference in proportions was (−0.0292, 0.0054), which contains zero, further supporting the conclusion that the true difference in proportions may be zero.

---

## Analysis 2: Mean Analysis (Welch's Two-Sample T-Test)

### What We Tested
Whether the mean alcohol use frequency score differed between male and female students.

`CurrentAlcoholUse` was treated as a continuous variable using its original 1–7 ordinal scale, where higher values indicate greater drinking frequency.

### Results

| | Male | Female |
|---|---|---|
| Sample size (n) | 6,425 | 6,234 |
| Mean score | 1.8139 | 1.9966 |
| Difference (Male − Female) | −0.1828 | |
| SE | 0.0230 | |
| T-statistic | −7.9389 | |
| P-value | < 0.0001 | |
| 95% CI for difference | (−0.2279, −0.1377) | |

### Interpretation
Female students reported a significantly higher mean alcohol use frequency score (1.9966) compared to male students (1.8139). The difference of −0.1828 was statistically significant (T = −7.9389, p < 0.0001 < 0.05). We therefore **reject H₀** and conclude that there is a statistically significant difference in mean alcohol use frequency between male and female students, with females drinking more frequently on average.

The 95% confidence interval for the difference in means was (−0.2279, −0.1377), which does not contain zero, confirming that the true difference is unlikely to be zero.

---

## Comparing the Two Analyses

| | Proportion Analysis | Mean Analysis |
|---|---|---|
| **Question** | Do they drink at all? | How often do they drink? |
| **Method** | Two-Proportion Z-Test | Welch's Two-Sample T-Test |
| **Result** | No significant difference | Significant difference |
| **p-value** | 0.1789 | < 0.0001 |
| **Decision** | Fail to reject H₀ | Reject H₀ |

The two analyses tell a nuanced story: while male and female students are **equally likely to drink** (proportion analysis), among those who do drink, **female students tend to drink more frequently** (mean analysis). This suggests that gender differences in adolescent alcohol use may be more apparent in drinking frequency than in drinking prevalence.

---

## Limitations

- `CurrentAlcoholUse` is measured on an ordinal scale (1–7); treating it as continuous in the mean analysis is an approximation.
- The YRBS uses a complex multi-stage sampling design; standard errors computed here do not account for survey weights, which may affect precision.
- Self-reported data may be subject to social desirability bias, potentially underreporting actual alcohol use.

---

## Conclusion

Based on the YRBS 2007 data, gender alone does not significantly predict whether a student currently drinks alcohol. However, among students who do drink, females report significantly higher drinking frequency than males. These findings highlight the importance of examining both prevalence and frequency when studying adolescent alcohol use behaviors.

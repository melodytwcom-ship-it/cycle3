# Summary

## Project Cycle 3 — Gender and Current Alcohol Use
**Group 13 | 113370219 謝紫旋, 113370232 周以心**

---

## Proportion Interpretation Draft

**Research Question**
Is the proportion of current alcohol use different between **male and female** students?

**中文：**
YRBS 2007 資料中，男女學生目前有飲酒習慣的比例是否有所不同？

**What was estimated or tested**
We estimated the population proportions of `CurrentAlcoholUse` (recoded as binary: 0 = non-drinker, 1 = current drinker) for male and female students, and tested whether the difference in proportions is significantly different from **0**.

**Main numerical results**
The sample size was **6,425** for male students and **6,234** for female students.
The sample proportion of current drinkers was **0.5273** for males and **0.5012** for females.
The observed difference (Male − Female) was **−0.0119**, with a standard error of **0.0088**.
The 95% confidence interval for the difference was approximately **(−0.0292, 0.0054)**.
The two-proportion z-test produced a test statistic of approximately **−1.3442** with a p-value of **0.1789**.

**What the confidence interval means**
This confidence interval gives a plausible range for the true difference in proportions of current alcohol use between male and female students in the YRBS 2007 population. Since the interval **(−0.0292, 0.0054)** contains zero, it suggests that the true difference in proportions could plausibly be zero. If this study were repeated many times, similarly constructed intervals would capture the true difference about 95% of the time.

**What the hypothesis test implies**
Using the benchmark value of **0 (no difference)**, the hypothesis test result was: **Fail to Reject H₀**. This means the sample does **not** provide enough evidence that the true proportion of current alcohol use is different between male and female students.

**Whether the inferential result is consistent with what we saw in EDA**
The descriptive statistics showed that male (52.73%) and female (50.12%) students had very similar proportions of current alcohol use, with only a 2.61 percentage point difference. The inferential result is consistent with this observation — the small numerical difference visible in the bar chart did not reach statistical significance, suggesting it may be due to random sampling variation rather than a true population difference.

**What should be interpreted cautiously**
The result should be interpreted carefully because the binary recoding of `CurrentAlcoholUse` (1 = non-drinker, 2–7 = drinker) treats students who drank on 1–2 days the same as those who drank all 30 days. This simplification may obscure meaningful differences in drinking intensity between groups.

---

## Mean Interpretation Draft

**Research Question**
Is the mean alcohol use frequency score different between **male and female** students?

**中文：**
YRBS 2007 資料中，男女學生的飲酒頻率平均分數是否有所不同？

**What was estimated or tested**
We estimated the population mean of `CurrentAlcoholUse` (original 1–7 ordinal scale, where higher values indicate greater drinking frequency) for male and female students, and tested whether the difference in means is significantly different from **0**.

**Main numerical results**
The sample size was **6,425** for male students and **6,234** for female students.
The sample mean alcohol use frequency score was **1.8139** for males and **1.9966** for females.
The observed difference (Male − Female) was **−0.1828**, with a standard error of **0.0230**.
The 95% confidence interval for the difference was approximately **(−0.2279, −0.1377)**.
The Welch's two-sample t-test produced a test statistic of approximately **−7.9389** with a p-value of **< 0.0001**.

**What the confidence interval means**
This confidence interval gives a plausible range for the true difference in mean alcohol use frequency between male and female students in the YRBS 2007 population. Since the entire interval **(−0.2279, −0.1377)** lies below zero, it suggests that the true mean frequency score for males is consistently lower than that for females. If this study were repeated many times, similarly constructed intervals would capture the true difference about 95% of the time.

**What the hypothesis test implies**
Using the benchmark value of **0 (no difference)**, the hypothesis test result was: **Reject H₀**. This means the sample provides **enough** evidence that the true population mean alcohol use frequency is different between male and female students, with females reporting significantly higher frequency on average.

**Whether the inferential result is consistent with what we saw in EDA**
The descriptive statistics showed that female students had a higher mean score (1.9966) compared to male students (1.8139), a difference of 0.1828. The inferential result is consistent with this observation — the difference visible in the bar chart was confirmed to be statistically significant, suggesting it reflects a true population difference rather than random sampling variation.

**What should be interpreted cautiously**
The result should be interpreted carefully because `CurrentAlcoholUse` is measured on an ordinal scale (1–7), and treating it as a continuous variable in the t-test is an approximation. Additionally, self-reported alcohol use data may be subject to social desirability bias, and the YRBS complex sampling design was not fully accounted for in the standard error calculations, which may affect the precision of the estimates.

# References & Analytical Decisions

## Project Cycle 3 — Gender and Current Alcohol Use
**Group 13 | 113370219 謝紫旋, 113370232 周以心**

---

## 1. 資料來源 | Data Source

**Dataset:** Youth Risk Behavior Surveillance System (YRBS) 2007

- **主辦單位:** Centers for Disease Control and Prevention (CDC)
- **原始檔案:** `YRBS_2007.csv`（共 14,041 筆，103 個變數）
- **官方網站:** https://www.cdc.gov/yrbs
- **官方報告:** CDC. (2008). *Youth Risk Behavior Surveillance — United States, 2007.* MMWR Surveillance Summaries, 57(SS-4). https://www.cdc.gov/mmwr/preview/mmwrhtml/ss5704a1.htm

---

## 2. 變數編碼 | Variable Coding

### Group Variable — `WhatIsYourSex`

根據 YRBS 2007 官方問卷編碼定義：

| 原始編碼 | 定義 | 本專題標籤 |
|----------|------|-----------|
| 1.0 | Male（男性） | `Male` |
| 2.0 | Female（女性） | `Female` |

> **來源:** `Question.ipynb` Section 2 Output 表格；`processed_data.py` 資料清理流程

---

### Response Variable — `CurrentAlcoholUse`

根據 YRBS 2007 官方問卷，題目為：
*"During the past 30 days, on how many days did you have at least one drink of alcohol?"*

| 原始編碼 | 定義 |
|----------|------|
| 1 | 0 days（未飲酒） |
| 2 | 1–2 days |
| 3 | 3–5 days |
| 4 | 6–9 days |
| 5 | 10–19 days |
| 6 | 20–29 days |
| 7 | All 30 days |

> **來源:** `05_mean_inference.ipynb` Section 2 資料清理說明；YRBS 2007 官方問卷

---

## 3. 分組定義 | Group Definition

- **分組變數:** `WhatIsYourSex`
- **Group 1:** Male（`WhatIsYourSex == 1.0`），n = 6,425
- **Group 2:** Female（`WhatIsYourSex == 2.0`），n = 6,234
- **排除條件:** 性別欄位或飲酒欄位任一為缺失值（NaN）者予以刪除

處理流程（參考 `processed_data.py`）：
```python
df_clean = df[['WhatIsYourSex', 'CurrentAlcoholUse']].dropna()
df_clean = df_clean[df_clean['WhatIsYourSex'].isin([1.0, 2.0])]
```

---

## 4. 反應變數定義 | Response Variable Definition

本專題對 `CurrentAlcoholUse` 採取**兩種詮釋方式**，分別對應兩種分析方法：

### 4a. Proportion Analysis（比例分析）
- 將 `CurrentAlcoholUse` **重編碼為 binary**：
  - `1`（0 days）→ `0`（non-drinker，未飲酒）
  - `2–7`（≥1 day）→ `1`（current drinker，有飲酒）
- **目的:** 比較男女「目前有飲酒習慣」的比例差異

```python
df_clean['alcohol_binary'] = np.where(
    df_clean['CurrentAlcoholUse'] == 1.0, 0, 1
)
```

### 4b. Mean Analysis（平均數分析）
- 保留 `CurrentAlcoholUse` **原始 1–7 連續數值**，視為有序尺度（ordinal scale）
- **目的:** 比較男女「飲酒頻率平均分數」的差異

> **來源:** `04_two-sample_inference.py`；`05_mean_inference.ipynb` Section 2

---

## 5. 方法選擇 | Method Selection

### 5a. Two-Proportion Z-Test（比例推論）

- **適用條件:** 反應變數為 binary（0/1），比較兩組比例
- **使用套件:** `statsmodels.stats.proportion.proportions_ztest`
- **檢定方向:** Two-sided（雙尾）
- **顯著水準:** α = 0.05

**假設（Hypotheses）:**

$$H_0: p_{male} - p_{female} = 0$$
$$H_1: p_{male} - p_{female} \neq 0$$

> **來源:** `Question.ipynb` Section 1 假設說明；OpenIntro Statistics Ch. 6

---

### 5b. Welch's Two-Sample T-Test（平均數推論）

- **適用條件:** 反應變數為連續／有序數值，比較兩組平均數
- **選擇 Welch's（不假設等變異數）原因:** 男女樣本數相近但不完全相等，保守起見不假設 σ₁² = σ₂²
- **使用套件:** `scipy.stats.ttest_ind(equal_var=False)`
- **檢定方向:** Two-sided（雙尾）
- **顯著水準:** α = 0.05

**假設（Hypotheses）:**

$$H_0: \mu_{male} - \mu_{female} = 0$$
$$H_1: \mu_{male} - \mu_{female} \neq 0$$

> **來源:** `05_mean_inference.ipynb` Section 4 & 5

---

## 6. 考慮的假設 | Assumptions Considered

### Two-Proportion Z-Test 假設

| 假設 | 是否滿足 | 說明 |
|------|---------|------|
| 隨機抽樣 | ✅ | YRBS 採用多階段隨機抽樣設計 |
| 獨立觀測 | ✅ | 每位受訪者獨立填答 |
| 樣本數足夠大 | ✅ | n_male = 6,425；n_female = 6,234，均遠大於 30 |
| np ≥ 10 且 n(1-p) ≥ 10 | ✅ | 兩組成功與失敗次數均遠大於 10 |

### Welch's Two-Sample T-Test 假設

| 假設 | 是否滿足 | 說明 |
|------|---------|------|
| 隨機抽樣 | ✅ | YRBS 採用多階段隨機抽樣設計 |
| 獨立觀測 | ✅ | 兩組（男/女）互相獨立 |
| 樣本數足夠大 | ✅ | n > 6,000，依中央極限定理可近似常態 |
| 不假設等變異數 | ✅ | 使用 Welch's T-Test（equal_var=False） |

---

## 7. 統計方法參考文獻 | Statistical References

- Diez, D., Çetinkaya-Rundel, M., & Barr, C. (2019). *OpenIntro Statistics* (4th ed.). OpenIntro. https://www.openintro.org/book/os/
- Seabold, S., & Perktold, J. (2010). Statsmodels: Econometric and statistical modeling with Python. *Proceedings of the 9th Python in Science Conference.*
- Virtanen, P., et al. (2020). SciPy 1.0: Fundamental algorithms for scientific computing in Python. *Nature Methods, 17*, 261–272. https://doi.org/10.1038/s41592-020-0772-5

---

## 8. 程式碼檔案對照 | Code File Reference

| 步驟 | 對應檔案 |
|------|---------|
| 研究問題與變數選取 | `notebook/Question.ipynb` |
| 資料清理與輸出 | `notebook/processed_data.py` |
| 描述統計 | `notebook/03_descriptive_statistics.ipynb` |
| 比例推論（Z-Test） | `notebook/04_two-sample_inference.ipynb` |
| 平均數推論（T-Test） | `notebook/05_mean_inference.ipynb` |

import pandas as pd
from pathlib import Path

# 取得目前 py 檔所在資料夾
current_dir = Path(__file__).resolve().parent

# 回到 project-cycle-3-main
project_path = current_dir.parent

# CSV 路徑
raw_path = project_path / "data" / "raw" / "YRBS_2007.csv"

# 輸出路徑
processed_path = (
    project_path
    / "data"
    / "processed"
    / "YRBS_2007_cleaned.csv"
)

# Debug 用
print("目前專案路徑：")
print(project_path)

print("\nCSV 路徑：")
print(raw_path)

# 讀取 CSV
df = pd.read_csv(raw_path)

# 只保留需要欄位
df_selected = df[
    ["WhatIsYourSex", "CurrentAlcoholUse"]
]

# 用平均值填補缺失值
df_cleaned = df_selected.fillna(
    df_selected.mean(numeric_only=True)
)

# 建立 processed 資料夾
processed_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

# 存檔
df_cleaned.to_csv(
    processed_path,
    index=False
)

print("\n檔案儲存成功！")
print(processed_path)
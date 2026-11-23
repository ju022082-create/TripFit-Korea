from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate the original dataset in the project folder
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = (
    BASE_DIR / "tourism_all.csv"
    if (BASE_DIR / "tourism_all.csv").exists()
    else BASE_DIR.parent / "tourism_all.csv"
)
OUTPUT_DIR = BASE_DIR / "eda_results"
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Load dataset
df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")

print("=== Dataset Profile ===")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")
print("Fields:", ", ".join(df.columns))

# 2. Missing values and duplicate IDs
missing = df.isna().sum().sort_values(ascending=False)
duplicates = df.duplicated(subset=["contentid"]).sum()

quality = pd.DataFrame(
    {
        "field": missing.index,
        "missing_count": missing.values,
        "missing_percent": (missing.values / len(df) * 100).round(2),
    }
)

quality.to_csv(OUTPUT_DIR / "data_quality.csv", index=False, encoding="utf-8-sig")

print("\n=== Data Quality ===")
print(quality.to_string(index=False))
print(f"Duplicate contentid: {duplicates}")

# 3. Category distribution
category = df["lclsSystm3"].fillna("Unknown").value_counts().head(10)

summary = category.rename_axis("category_code").reset_index(name="count")

summary.to_csv(OUTPUT_DIR / "category_summary.csv", index=False, encoding="utf-8-sig")

print("\n=== Top 10 Category Codes ===")
print(summary.to_string(index=False))

# 4. Visualization
plt.figure(figsize=(10, 6))
plt.barh(summary["category_code"][::-1], summary["count"][::-1])
plt.xlabel("Number of tourist attractions")
plt.ylabel("Tourism category code")
plt.title("Top 10 Tourism Categories in Korea")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "category_distribution.png", dpi=200)
plt.close()

print("\nEDA completed successfully.")
print(f"Results saved to: {OUTPUT_DIR}")

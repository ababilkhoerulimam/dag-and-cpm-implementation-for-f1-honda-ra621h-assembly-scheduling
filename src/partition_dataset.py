import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, "data", "Honda_RA621H_Assembly_Dataset.xlsx")
OUTPUT_DIR = os.path.join(BASE_DIR, "results", "output_csv")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Components 
df_components = pd.read_excel(INPUT_FILE, sheet_name="Components", header=2)
df_components.to_csv(os.path.join(OUTPUT_DIR, "components.csv"), index=False)
print(f"[1] components.csv  ->  {df_components.shape[0]} baris, {df_components.shape[1]} kolom")

# 2. Dependency Edges
df_edges = pd.read_excel(INPUT_FILE, sheet_name="Dependency_Edges", header=2)
df_edges.to_csv(os.path.join(OUTPUT_DIR, "dependency_edges.csv"), index=False)
print(f"[2] dependency_edges.csv  ->  {df_edges.shape[0]} baris, {df_edges.shape[1]} kolom")

# 3. Summary Stats
# Sheet ini tidak punya header baris tunggal, kita baca apa adanya
df_summary = pd.read_excel(INPUT_FILE, sheet_name="Summary_Stats", header=None)
df_summary.to_csv(os.path.join(OUTPUT_DIR, "summary_stats.csv"), index=False, header=False)
print(f"[3] summary_stats.csv  ->  {df_summary.shape[0]} baris, {df_summary.shape[1]} kolom")

print(f"\nSemua file CSV tersimpan di folder: {OUTPUT_DIR}")
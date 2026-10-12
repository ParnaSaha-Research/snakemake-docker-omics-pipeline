import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("results", exist_ok=True)
df = pd.read_csv("results/its_summary_table.csv")

def extract_genus(header):
    parts = header.split()
    if len(parts) >= 3:
        return parts[2]
    return "Unknown"

df['Genus'] = df['Full_Header'].apply(extract_genus)

sns.set_theme(style="whitegrid")

# Plot 1: Genus distribution
plt.figure(figsize=(10, 6))
genus_counts = df['Genus'].value_counts()
sns.barplot(x=genus_counts.values, y=genus_counts.index, hue=genus_counts.index, palette="viridis", legend=False)
plt.title("Fungal Genus Distribution (n=34)", fontsize=14, fontweight='bold')
plt.xlabel("Isolate Count", fontsize=12)
plt.ylabel("Genus", fontsize=12)
plt.tight_layout()
plt.savefig("results/genus_distribution_plot.png", dpi=300)
plt.close()

# Plot 2: Length distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['Length_bp'], kde=True, color="teal", bins=10)
plt.title("ITS Sequence Length Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Length (bp)", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.tight_layout()
plt.savefig("results/length_distribution_plot.png", dpi=300)
plt.close()

print("Visualization complete! Check your results/ folder for the generated PNG plots.")

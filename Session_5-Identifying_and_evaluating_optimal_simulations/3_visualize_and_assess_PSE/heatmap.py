import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from os import makedirs

### START MODIFYING HERE
### ====================================

# Define file names and directories
sublist = "../../Session_4-Jobs_and_PSE/subs.tsv"  # where our sublist is
results_file_pattern = "../2_PSE_all_metrics/outputs/results/simulation_results/{subject}_simulation_results.txt"  # where our PSE results files are
img_file_pattern="heatmaps/{subject}_PSE_heatmap_{metric}.png" #where we want heatmaps saved to
makedirs("heatmaps",exist_ok=True)

### STOP MODIFYING HERE
### ====================================


# Read the list of subjects from the log file
with open(sublist, "r") as file:
    sublist = [line.strip() for line in file]

# Metrics to plot
metrics = ['FCD_var', 'FCD_KS', 'FC_corr', 'FCDvar_diff']
column_indices = [8, 9, 10, 11]


# Process each subject
for subject in sublist:
    print(f"Processing subject: {subject}")

    # Read data from the CSV file
    data_path = results_file_pattern.format(subject=subject)
    data = pd.read_csv(data_path, sep="\s+", header=None, usecols=[1, 2] + column_indices, names=["noise", "G"] + metrics)

    # Process each metric
    for metric, column_index in zip(metrics, column_indices):
        print(f"Processing metric: {metric}")

        # Initialize dictionaries to store maximum value and NaN values for each (noise, G) pair
        values = {}
        nan_values = {}

        # Update dictionaries
        for _, row in data.iterrows():
            key = (row["noise"], row["G"])
            value = row[metric]

            # If the value is 'nan', update nan_values
            if pd.isna(value):
                nan_values[key] = 1  # Mark it as 1
                values[key] = 0
            else:
                # Otherwise, update values if current value is greater
                if (key not in values) or (values[key] < value):
                    values[key] = value
                    if key in nan_values:
                        del nan_values[key]

        print(f"NaN values for {metric}: {nan_values}")

        # Convert dictionaries to dataframes for plotting
        df = pd.DataFrame(values.values(), index=pd.MultiIndex.from_tuples(values.keys(), names=["noise", "G"])).reset_index()
        pivot_table = df.pivot("noise", "G", 0)

        # Plot heatmap
        fig, ax = plt.subplots(figsize=(10, 8))
        cmap = plt.cm.YlGnBu(np.linspace(0, 1, 256))
        cmap[0] = (1, 0, 0, 1)  # Red for NaN
        cmap = plt.cm.colors.LinearSegmentedColormap.from_list("custom", cmap, 256)

        sns.heatmap(pivot_table, ax=ax, cmap=cmap, cbar_kws={'label': metric}, mask=pivot_table.isnull(), annot=False)
        plt.title(f"Heatmap for {metric} based on Noise and G")
        plt.tight_layout()
        plt.savefig(img_file_pattern.format(subject=subject, metric=metric))
        plt.show()
        plt.clf()

print("Done!")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

### START MODIFYING HERE
### ====================================

# Define file names and directories
sublist = "/home/jneudorf/scratch/TVB_jobs/tvb_study_group/Session_4-Jobs_and_PSE/subs.tsv" #where are sublist is
results_folder = "/home/jneudorf/scratch/TVB_jobs/tvb_study_group/Session_4-Jobs_and_PSE/results/simulation_results"
results_file_pattern=results_folder+"/{subject}_simulation_results.txt" #where our PSE results files are
img_file_pattern=results_folder+"/{subject}_PSE_heatmap.png" #where we want heatmaps saved to

### STOP MODIFYING HERE
### ====================================


# Read the list of subjects from the log file
with open(sublist, "r") as file:
    sublist = [line.strip() for line in file]

# Initialize empty dataframe for aggregate measures at end
subjects_data = pd.DataFrame()
# Process each subject
for subject in sublist:
    print(f"Processing subject: {subject}")

    # Read data from the CSV file
    data_path = results_file_pattern.format(subject=subject)
    data = pd.read_csv(data_path, sep="\s+", header=None, usecols=[1, 2, 8], names=["noise", "G", "FCD_var"])
    data_tmp = data
    data_tmp['subject'] = subject
    data_tmp['FCD_rank'] = data_tmp['FCD_var'].rank(na_option='top')
    subjects_data = subjects_data.append(data_tmp)
    
    # Initialize dictionaries to store maximum FCD_var and NaN values for each (noise, G) pair
    fcd_values = {}
    nan_values = {}

    # Update fcd_values and nan_values dictionaries
    for _, row in data.iterrows():
        key = (row["noise"], row["G"])

        # If the value is 'nan', update nan_values
        if str(row["FCD_var"]).strip()=='nan':
            if key not in fcd_values:
                nan_values[key] = 1 #Mark it as 1
                fcd_values[key] = 0
        else:
            # Otherwise, update fcd_values if current FCD_var is greater
            if (key not in fcd_values) or (fcd_values[key] < row["FCD_var"]):
                fcd_values[key] = row["FCD_var"]
                if key in nan_values:
                    del nan_values[key]
    print(f"NaN values: {nan_values}")

    # Convert dictionaries to dataframes for plotting
    df = pd.DataFrame(fcd_values.values(), index=pd.MultiIndex.from_tuples(fcd_values.keys(), names=["noise", "G"])).reset_index()
    pivot_table = df.pivot("noise", "G", 0)

    df_nan = pd.DataFrame(nan_values.values(), index=pd.MultiIndex.from_tuples(nan_values.keys(), names=["noise", "G"])).reset_index()
    pivot_table_nan = df_nan.pivot("noise", "G", 0) if not df_nan.empty and "noise" in df_nan.columns and "G" in df_nan.columns else None

    # Plot heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    cmap = plt.cm.YlGnBu(np.linspace(0, 1, 256))
    cmap[0] = (1, 0, 0, 1)
    cmap = plt.cm.colors.LinearSegmentedColormap.from_list("custom", cmap, 256)

    sns.heatmap(pivot_table, ax=ax, cmap=cmap, cbar_kws={'label': 'FCD_var'}, mask=pivot_table.isnull(), annot=False)
    print(pivot_table_nan)

    plt.title("Heatmap for FCD_var based on Noise and G")
    plt.tight_layout()
    plt.savefig(img_file_pattern.format(subject=subject))
    plt.show()
    plt.clf()

    
# Aggregate measures and ideal values table
optimal_parameters = pd.DataFrame()
for subject in sublist:
    FCD_rank = subjects_data.loc[subjects_data['subject'] == subject]['FCD_var'].idxmax(skipna=True)

    idxmax = subjects_data.loc[subjects_data['subject'] == subject]['FCD_var'].idxmax(skipna=True)
    max_row = subjects_data.loc[subjects_data['subject'] == subject].iloc[idxmax]
    optimal_parameters = optimal_parameters.append(max_row)[['subject','noise','G','FCD_var']]
optimal_parameters.to_csv(f'{results_folder}/optimal_parameters.csv',index=False)
    
# Below not working properly
rank_mean_mat = subjects_data.groupby(['noise','G'])['FCD_rank'].mean().unstack()
fig, ax = plt.subplots(figsize=(10, 8))
cmap = plt.cm.YlGnBu(np.linspace(0, 1, 256))
cmap = plt.cm.colors.LinearSegmentedColormap.from_list("custom", cmap, 256)

sns.heatmap(rank_mean_mat, ax=ax, cmap=cmap, cbar_kws={'label': 'FCD_var_rank'}, annot=False)
print(pivot_table_nan)

plt.title("Heatmap for FCD_rank mean across subjects based on Noise and G (higher rank is better)")
plt.tight_layout()
plt.savefig(f'{results_folder}/FCD_rank_mean.png')
plt.show()
plt.clf()
    
print("Done!")

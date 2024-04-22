import pandas as pd

### START MODIFYING HERE
### ====================================

# Define file names and directories
sublist = "/path/to/subs.tsv"  # where our sublist is
results_file_pattern = "path/to/{subject}_simulation_results.txt"  # where our PSE results files are
output_file_pattern = "/path/to/save/optimal_{metric}_for_each_subject.tsv"  # where we save results

### STOP MODIFYING HERE
### ====================================

# Read the list of subjects from the log file
with open(sublist, "r") as file:
    subjects = [line.strip() for line in file]

# Metrics to plot
metrics = ['FCD_var', 'FCD_KS', 'FC_corr', 'FCDvar_diff']
column_indices = [8, 9, 10, 11]

# Prepare a dictionary to store results for each metric
results = {metric: [] for metric in metrics}

# Process each subject
for subject in subjects:
    print(f"Processing subject: {subject}")

    # Read data from the CSV file
    data_path = results_file_pattern.format(subject=subject)
    data = pd.read_csv(data_path, sep="\s+", header=None, usecols=[1, 2] + column_indices, names=["noise", "G"] + metrics)

    # Find maximum values for each metric
    for metric in metrics:
        max_row = data.loc[data[metric].idxmax()]
        results[metric].append([subject, max_row['noise'], max_row['G'], max_row[metric]])

# Save results to files for each metric
for metric in metrics:
    df = pd.DataFrame(results[metric], columns=['Subject', 'Noise', 'G', 'Optimal_' + metric])
    df.to_csv(output_file_pattern.format(metric=metric), sep='\t', index=False)

print("Done!")

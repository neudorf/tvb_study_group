#!/bin/bash
# This script submits the optimal parameter simulation for each subject.

### START MODIFYING HERE
### ====================================
# Location of your submission script directory
SUBMISSION_SCRIPT_DIR='../../Session_4-Jobs_and_PSE'

PARAM_FILE="../3_visualize_and_assess_PSE/optimal_params/optimal_FCD_var_for_each_subject.tsv"

# List of subjects
sublist="${SUBMISSION_SCRIPT_DIR}/subs.tsv"

# Path to a subject's weights matrix txt file - the {subject} portion will be replaced dynamically in the python script
weights_file_pattern="${SUBMISSION_SCRIPT_DIR}/subs/{subject}/weights.txt"

# location of new outputs
OUTPUTS_DIR='outputs'
mkdir $OUTPUTS_DIR

# Output directory and file for saving simulation results
results_dir="${OUTPUTS_DIR}/results/simulation_results"
mkdir -p $results_dir
results_file_pattern="${results_dir}/{subject}_simulation_results.txt"

# Output directory and file for saving FCD matrices
FCD_dir="${OUTPUTS_DIR}/results/FCD_matrices"
FCD_file_pattern="${FCD_dir}/{subject}/{subject}_{noise}_{G}_{dt}_FCD.txt"

# Logging directory for saving any printouts from the jobs (e.g. errors)
log_dir="${OUTPUTS_DIR}/logs"

# Location of empirical functional feature files (FC, FCD, FCDvar)
empFUNC_dir="../1_empirical_functional_features/empFUNC/saves"

# Parameter ranges
G_start=1.65
G_end=2.05
num_G=41

noise_start=0.02
noise_end=0.05
num_noise=7

dt=0.005

# simulation length (unit depends on model setup) - desired length of simulated time series - not to be confused with time_per_sim
sim_len=30000

# Number of simulations per job
num_sims_per_job=3

# Time per simulation (seconds) - max amount of time you want your simulation script to run for - not to be confused with sim_len
time_per_sim=1000

### ====================================
### STOP MODIFYING HERE

mkdir -p "${FCD_dir}/"
mkdir -p "${log_dir}/"
mkdir -p "${sim_dir}/"

total_lines=$(wc -l < "$PARAM_FILE")
num_jobs=$(( (total_lines + num_sims_per_job - 1) / num_sims_per_job ))  # Calculate the number of jobs needed

sbatch -J "optimal_parameters_rerun" --array=1-$num_jobs \
  -o "${log_dir}/optimal_parameters_rerun_job_%a.out" \
  optimal_sim_job.sh $PARAM_FILE $num_sims_per_job $time_per_sim $weights_file_pattern $results_file_pattern $FCD_file_pattern $empFUNC_dir $dt $sim_len $sim_file_pattern

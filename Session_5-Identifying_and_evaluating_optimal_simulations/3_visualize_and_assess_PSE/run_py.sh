#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --account=def-rmcintos
#SBATCH --mem-per-cpu=8GB
#SBATCH --cpus-per-task=1
#SBATCH --mail-user=jneudorf@sfu.ca

module load StdEnv/2020
module load scipy-stack/2020b
module load python/3.7.7
. ~/TVB/virtual_aging_brain/env/bin/activate
python optimal_parameters_getter.py
python heatmap.py

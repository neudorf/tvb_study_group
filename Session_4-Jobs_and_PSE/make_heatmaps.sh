#!/bin/bash
#SBATCH --account=def-rmcintos
#SBATCH --mem=2000MB
#SBATCH --time=0-1:00

module load StdEnv/2020 scipy-stack
. ~/TVB/virtual_aging_brain/env/bin/activate

python3 heatmap.py

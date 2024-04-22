#!/bin/bash
#SBATCH --account=<ACCOUNT>
#SBATCH --mail-user=<EMAIL>
#SBATCH --mail-type=FAIL
#SBATCH --mem=8000MB
#SBATCH --time=0-6:00


## TO EDIT HERE
## =============================
module load scipy-stack/2023b
. ~/TVB/virtual_aging_brain/env/bin/activate
## =============================
## TO EDIT HERE

python create_emp_funcfeat.py $1

#!/bin/bash
#SBATCH --account=rrg-rmcintos
#SBATCH --mail-user=jneudorf@sfu.ca
#SBATCH --mail-type=FAIL
#SBATCH --mem=8000MB
#SBATCH --time=0-6:00


## TO EDIT HERE
## =============================
module load StdEnv/2020
module load scipy-stack/2020b
module load python/3.7.7
. ~/TVB/virtual_aging_brain/env/bin/activate
## =============================
## TO EDIT HERE

python create_emp_funcfeat.py $1

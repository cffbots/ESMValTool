#!/bin/bash -e
###############################################################################
### BATCH SCRIPT TO RUN THE ESMVALTOOL AT DKRZ MISTRAL
### Author: Mattia Righi (DLR)
###############################################################################
#SBATCH --partition=compute
#SBATCH --time=1:00:00
#SBATCH --mail-type=FAIL
#SBATCH --account=bd1083
#SBATCH --output=job_%j.out.log
#SBATCH --error=job_%j.err.log
###############################################################################

# Submit job with: sbatch job_DKRZ-MISTRAL.sh

# Input arguments
RECIPE=/work/bd0854/b380971/tools4/ESMValTool/esmvaltool/recipes/galytska21/recipe_Arctic_telecon_qbo_era5_vs_ei.yml
CONFIG=/work/bd0854/b380971/tools4/ESMValTool/config-user_EG.yml

# Set environment
CONDAPATH=/mnt/lustre01/pf/b/b380971/mambaforge

# Changes below this line should not be required
source $CONDAPATH/etc/profile.d/conda.sh
conda activate esmvaltool_v24
conda info --envs

esmvaltool run --config-file $CONFIG $RECIPE

#!/bin/bash
#SBATCH --partition work
#SBATCH --time 02:00
#SBATCH --mem=200G
#SBATCH --nodes=2

# Just happens to be the name of the module for GNU parallel on this system.
module load parallel/20220522

srun --nodes=2 --ntasks=2 --cpus-per-task=1 parallel ./dummy_program.sh {1} ::: dummy_arg1 dummy_arg2

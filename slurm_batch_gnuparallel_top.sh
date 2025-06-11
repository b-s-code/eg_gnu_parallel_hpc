#!/bin/bash
#SBATCH --partition work
#SBATCH --time 02:00
#SBATCH --mem=1G
#SBATCH --nodes=2

module load parallel/20220522

# Dummy args are unused.  Just employing them to cause multiple processes to be spawned.
parallel srun --nodes=1 --ntasks=1 --cpus-per-task=1 ./dummy_program.sh {1} ::: dummy_arg1 dummy_arg2

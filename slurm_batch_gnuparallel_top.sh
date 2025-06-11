#!/bin/bash
#SBATCH --partition work
#SBATCH --time 02:00
#SBATCH --mem=200G
#SBATCH --nodes=2

# Just happens to be the name of the module for GNU parallel on this system.
module load parallel/20220522

# Dummy args are unused.  Just employing them to cause multiple processes to be spawned.
parallel srun --nodes=1 --ntasks=1 --cpus-per-task=1 ./dummy_program.sh {1} ::: dummy_arg1 dummy_arg2

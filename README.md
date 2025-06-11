# Small examples of integrating GNU Parallel with Slurm

There are many other ways to achieve parallel process execution on HPC systems but I wanted to sketch out how GNU Parallel can integrate with Slurm.

This examples **do not intend to represent best practice**.

Rather they just sketch minimum examples.

Broadly, there are 2 approaches to consider.

1. Calling `parallel` from a slurm command.
2. Calling a slurm command from `parallel`.

Basically I want to see how to do each of these across more than 1 node.

## Relevant scripts

| Script | Purpose |
|---|---|
| `watch_squeue.sh`|For monitoring jobs, especially for watching number of nodes in use. |
| `slurm_batch_gnuparallel_top.sh` | Demonstrates using GNU parallel to call `srun`. |
| `slurm_batch_gnuparallel_bottom.sh` | Demonstrates using `srun` to call GNU parallel. |

### Note

Remember to call the slurm batch scripts as `sbatch <path/to/script>` so they actually get submitted to the scheduler, and so they don't just run on login node.

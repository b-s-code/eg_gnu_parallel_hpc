# Small examples of integrating GNU Parallel with Slurm

There are many other ways to achieve parallel process execution on HPC systems but I wanted to sketch out how GNU Parallel can integrate with Slurm.

**These scripts should absolutely not be used as example of good practice.**

Rather I just wanted to sketch minimum examples of 2 different approaches to show they each "work".

1. Calling `parallel` from `srun`.
2. Calling `srun` from `parallel`.

In particular, I wanted to see how to do each of these across more than 1 node.

For anyone wanting to actually see how to do thing kind of thing properly, there are **many** better examples of using GNU Parallel in combination with Slurm which can be revealed by a web search.

## Relevant scripts

| Script | Purpose |
|---|---|
| `watch_squeue.sh`| For monitoring jobs, especially for watching number of nodes in use. |
| `slurm_batch_gnuparallel_top.sh` | Demonstrates using GNU parallel to call `srun`. |
| `slurm_batch_gnuparallel_bottom.sh` | Demonstrates using `srun` to call GNU parallel. |

### Note to self

Remember to call the slurm batch scripts as `sbatch <path/to/script>` so they actually get submitted to the scheduler, and so they don't just run on login node.

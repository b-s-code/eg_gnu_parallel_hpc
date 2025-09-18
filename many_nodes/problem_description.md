# Spreading a set of OpenMalaria executions across more than one HPC node.

## Problem

Suppose you have more simulations to run than a node has cores.

Suppose you want to run that set of simulations *in less human time than it would take using a single node*.

Then you need a way to run more simulations at once than can fit on the cores of a single node.

This is the problem to solve.

## Solution

There are many ways to solve this problem.

The particular solution tactic here is:

1. Assume a value for NUM_CORES_PER_NODE, the number of cores each node has available for computation.  In the case of Setonix, take 128 for this value (nodes on the work partition have 2 x 64 CPU cores).

2. Assume a text file exists that contains *all* simulation commands to be run.  It is assumed that every input/output file name is unique - other than that they don't have to follow any pattern.

3. Make an assumption for the number of hours, NUM_HOURS_PER_NODE, that each node will be needed for.  May be hard to know in advance without a little testing.

4. Split the commands.txt into sub-lists, each of length NUM_CORES_PER_NODE or less (final list in particular is likely to contain the "remainder" of simulation commands. 

5. Instruct each node allocated to run exactly one sub-list of the commands. 

E.g.

Suppose you have the following `commands.txt` file, with 132 simulation commands.  You can use completely different file names.

```
./openMalaria -s scenario_a0.xml -o Azero.txt
./openMalaria -s scenario_a1.xml -o Aone.txt
./openMalaria -s scenario_a2.xml -o Atwo.txt
./openMalaria -s scenario_a3.xml -o Athree.txt
...
./openMalaria -s scenario_a126.xml -o Aonehundredandtwentysix.txt
./openMalaria -s scenario_a127.xml -o Aonehundredandtwentyseven.txt
./openMalaria -s scenario_a128.xml -o Aonehundredandtwentyeight.txt
./openMalaria -s scenario_a129.xml -o Aonehundredandtwentyeight.txt
./openMalaria -s scenario_xyz000.xml -o x_y_z_000.txt
./openMalaria -s scenario_xyz001.xml -o x_y_z_001.txt
./openMalaria -s scenario_xyz002.xml -o x_y_z_002.txt
```

We then just need to pass the path to commands.txt to our script that will manage the allocation of many nodes and the submission of simulation jobs to those nodes.

```
python3 spread_simulations.py /path/to/commands.txt
```

The values we assume for NUM_CORES_PER_NODE and NUM_HOURS_PER_NODE are hardcoded in spread_simulations.py and can be edited.

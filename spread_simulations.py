"""
Does not have to run on a compute node.
"""
import sys
import subprocess
import math

# Adjust as needed.  This is the value at time of writing for the HPC system this code was first written for.
NUM_CORES_PER_NODE = 128

# Adjust as needed.  Ideally, you should estimate this by testing duartion of a small number of simulations, or even just one simulation.
# If this value is too small, some simulations won't finish before the allocation expires.
# If this value is too large, you might wait longer than needed to get allocated nodes.
# Non-integer values are not supported at this time.
# TODO : currently unused by salloc call.
NUM_HOURS_PER_NODE = 1

def main():
    path_to_cmds = sys.argv[1]

    cmd_lines = []
    with open(path_to_cmds, 'r') as f:
        cmd_lines = f.readlines()

    # If there are any blank lines, filter them out now so they don't get "run".
    # No more validation than that is performed though.
    cmd_lines = [l for l in cmd_lines if l != '']

    num_cmds = len(cmd_lines)

    num_nodes_required = math.ceil(num_cmds / NUM_CORES_PER_NODE)

    for node_index in range(num_nodes_required):
        salloc_cmd = ['salloc',
            '--verbose',
            '-p', 'work',
            '-n', '1', # Hopefully the notion of a "task" can largely be ignored and we can just have one task per node.
            '-N', '1', # Important: we only ask for one node at a time.
            '-c', str(NUM_CORES_PER_NODE),
            '--exclusive',
            '-A', '$PAWSEY_PROJECT', # TODO : may have to be more careful here if environment variable does not get dereferenced.
            'python3', 'per_node.py', # Everything after this is args to per_node.py.
            str(path_to_cmds),
            str(node_index),
            str(NUM_CORES_PER_NODE)
        ]
        print("salloc_cmd:", salloc_cmd)

        # Use Popen instead of run since it is non-blocking.
        subprocess.Popen(salloc_cmd,
            # Used so that arguments in salloc command like $PAWSEY_PROJECT are interpreted by shell.
            shell=True)

if __name__ == "__main__":
    main()

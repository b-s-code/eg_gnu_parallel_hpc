"""
Should be run only on a compute node.
"""
import sys
import subprocess

def main():
    path_to_cmds = sys.argv[1]

    # Will be used to determine *which* sections of the command list to run.
    # Error checking on this value will not be done here.
    # That's caller's problem.
    node_number = sys.argv[2]

    # This value should be communicated from caller script.
    # Reasons for this design choice is to avoid fragility of having same value
    # hardcoded in multiple scripts and needing to have the same value in each.
    num_cores_per_node = sys.argv[3]

    cmd_lines = []
    with open(path_to_cmds, 'r') as f:
        cmd_lines = f.readlines()

    # If there are any blank lines, filter them out now so they don't get "run".
    # No more validation than that is performed though.
    cmd_lines = [l for l in cmd_lines if l != '']

    # Need to determine which part of the command list this node is
    # responsible for executing.
    cmd_index_lower_bound = node_number * num_cores_per_node
    cmd_index_upper_bound = (node_number + 1) * num_cores_per_node
    cmds_to_run_this_node = cmd_lines[
            cmd_index_lower_bound : cmd_index_upper_bound + 1
    ]

    # Now let's actually run the commands.
    for cmd in cmds_to_run_this_node:
        cmd_parts = cmd.rstrip().split(' ')

        # Use Popen instead of run since it is non-blocking.
        subprocess.Popen(cmd_parts)

if __name__ == "__main__":
    main()

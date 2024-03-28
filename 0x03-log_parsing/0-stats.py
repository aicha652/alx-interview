#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics"""


def print_stat(size, states):
    """Definition of print_stat function"""
    print("File size: {}".format(size))
    for state in sorted(states):
        print("{}: {}".format(state, states[state]))


if __name__ == "__main__":
    import sys

    file_size = 0
    states_dict = {}
    Acceptable = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stat(file_size, states_dict)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                file_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in Acceptable:
                    if states_dict.get(line[-2], -1) == -1:
                        states_dict[line[-2]] = 1
                    else:
                        states_dict[line[-2]] += 1
            except IndexError:
                pass
        print_stat(file_size, states_dict)
    except KeyboardInterrupt:
        print_stat(file_size, states_dict)
        raise
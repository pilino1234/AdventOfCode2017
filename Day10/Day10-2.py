from functools import reduce
from operator import xor

if __name__ == "__main__":
    with open("input.txt") as f:
        in_data = [ord(x) for x in f.readline().strip()]

    # in_data = [ord(x) for x in "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"]
    # in_data = []

    in_data += [17, 31, 73, 47, 23]

    proc_list = [i for i in range(256)]

    curr_pos = 0
    skip = 0
    for _ in range(64):
        for length in in_data:

            temp = []
            for i in range(curr_pos, curr_pos + length):
                temp.append(proc_list[i % len(proc_list)])
            for j in range(length):
                proc_list[(curr_pos + j) % len(proc_list)] = temp[-j - 1]

            curr_pos += length + skip
            curr_pos %= 256

            skip += 1

    dense_hash = []

    for group_start in range(0, len(proc_list), 16):
        group = proc_list[group_start:group_start + 16]
        dense_hash.append('%02x' % reduce(xor, group))

    print(''.join(dense_hash))

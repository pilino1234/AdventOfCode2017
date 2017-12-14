from functools import reduce
from operator import xor


def generate_disk(x, y):
    d = []

    for i in range(y):
        d.append(list(0 for _ in range(x)))

    return d


def knot_hash(key):
    in_data = [ord(x) for x in key.strip()]
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

    b_hash = ""

    for g in dense_hash:
        b_hash += '{0:08b}'.format(int(g, 16))

    return b_hash


def load_data(d, key):

    for row in range(len(d)):
        row_key = key + "-" + str(row)
        row_hash = knot_hash(row_key)
        for col in range(len(d[row])):
            d[row][col] = int(row_hash[col])

    return d


def count_used(disk):
    return sum(sum(row) for row in disk)


def count_groups(disk):

    seen = set()
    n = 0

    def dfs(i, j):
        if (i, j) in seen:
            return
        if not disk[i][j]:
            return
        seen.add((i, j))
        if i > 0:
            dfs(i-1, j)
        if j > 0:
            dfs(i, j-1)
        if i < len(disk)-1:
            dfs(i+1, j)
        if j < len(disk[i])-1:
            dfs(i, j+1)

    for i in range(len(disk)):
        for j in range(len(disk[i])):
            if (i, j) in seen:
                continue
            if not disk[i][j]:
                continue
            n += 1
            dfs(i, j)

    return n


if __name__ == "__main__":
    key_string = "hxtvlmkl"
    # key_string = "flqrgnkx"

    disk = generate_disk(128, 128)

    disk = load_data(disk, key_string)

    print(count_used(disk))

    print(count_groups(disk))

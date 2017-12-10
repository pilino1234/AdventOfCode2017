
def knot_hash(in_data, lengths):
    curr_pos = 0
    skip_size = 0

    working_lst = in_data[:]

    for length in lengths:

        temp = []
        for i in range(curr_pos, curr_pos + length):
            temp.append(working_lst[i % len(working_lst)])
        for j in range(length):
            working_lst[(curr_pos + j) % len(working_lst)] = temp[-j - 1]

        curr_pos += length + skip_size
        curr_pos %= 256

        skip_size += 1

    return working_lst


if __name__ == "__main__":
    with open("input.txt") as f:
        lengths = [int(n) for n in f.readline().split(",")]

    circle = [i for i in range(256)]

    hashed = knot_hash(circle, lengths)

    print(hashed[0] * hashed[1])

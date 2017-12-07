
def jump_until_escape(instrux):
    curr_idx = 0

    steps = 0

    while curr_idx < len(instrux):
        next_idx = curr_idx + instrux[curr_idx]
        instrux[curr_idx] += 1
        curr_idx = next_idx
        steps += 1

    return steps


def jump_until_escape_2(instrux):
    curr_idx = 0

    steps = 0

    while curr_idx < len(instrux):
        next_idx = curr_idx + instrux[curr_idx]

        if instrux[curr_idx] >= 3:
            instrux[curr_idx] -= 1
        else:
            instrux[curr_idx] += 1

        curr_idx = next_idx
        steps += 1

    return steps


if __name__ == "__main__":
    with open("input.txt") as f:
        read_offsets = f.readlines()

    offsets = [int(i) for i in read_offsets]

    print(jump_until_escape(offsets[:]))

    print(jump_until_escape_2(offsets[:]))

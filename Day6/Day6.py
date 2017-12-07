

def find_largest_bank(banks):
    largest_idx = 0

    for idx, val in enumerate(banks):
        if val > banks[largest_idx]:
            largest_idx = idx

    return largest_idx


def redist_in_banks(banks):
    blen = len(banks)

    idx = find_largest_bank(banks)

    val_to_redist = banks[idx]
    banks[idx] = 0

    while val_to_redist > 0:
        banks[(idx + 1) % blen] += 1
        val_to_redist -= 1
        idx += 1

    return banks


def redist_until_inf(banks):
    states = []

    while banks not in states:
        states.append(banks)
        banks = redist_in_banks(banks[:])

    return banks, len(states)


if __name__ == "__main__":
    # input = [0, 2, 7, 0]
    input_data = [10, 3, 15, 10, 5, 15, 5, 15, 9, 2, 5, 8, 5, 2, 3, 6]

    redist_banks, steps = redist_until_inf(input_data)
    print(redist_banks, steps)

    print(redist_until_inf(redist_banks))

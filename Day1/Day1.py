
def get_repeating(digits):
    length = len(digits)
    rep = []

    for idx, val in enumerate(digits):
        if val == digits[(idx + 1) % length]:
            rep.append(int(val))

    return rep


def get_opposite_repeating(digits):
    length = len(digits)
    half_length = length // 2
    rep = []

    for idx, val in enumerate(digits):
        if val == digits[(idx + half_length) % length]:
            rep.append(int(val))

    return rep


if __name__ == "__main__":
    with open("input.txt") as file:
        input_digits = file.read()

    print(sum(get_repeating(input_digits)))
    print(sum(get_opposite_repeating(input_digits)))

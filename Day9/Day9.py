
def remove_garbage(in_stream):
    out = ""

    curr_garbage = False
    skip = False

    garbage_count = 0

    for char in in_stream:
        if skip:
            skip = False
            continue

        if char == "!":
            skip = True
            continue

        if char == "<" and not curr_garbage:
            curr_garbage = True
            continue

        if char == ">" and curr_garbage:
            curr_garbage = False
            continue

        if not curr_garbage:
            out += char

        if curr_garbage:
            garbage_count += 1

    print("(Part 2) Garbage characters removed:", garbage_count)

    return out


def count_score(groups):
    pts = 0
    depth = 1

    for char in groups:
        if char == "{":
            depth += 1

        if char == "}":
            depth -= 1
            pts += depth

    return pts


if __name__ == "__main__":
    with open("input.txt") as f:
        read_stream = f.readline()

    # read_stream = "{{<a!>},{<a!>},{<a!>},{<ab>}}"

    # print(read_stream)

    cleaned = remove_garbage(read_stream)

    # print(cleaned)

    score = count_score(cleaned)

    print("(Part 1) Score:", score)

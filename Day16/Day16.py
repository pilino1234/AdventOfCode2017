from collections import deque


def build_dancefloor(progs):
    return [chr(97 + i) for i in range(progs)]


def spin(df, size):
    # return [deque(df).rotate(size)]
    return df[-size:] + df[:-size]


def exchange(df, idx1, idx2):
    df[idx1], df[idx2] = df[idx2], df[idx1]
    return df


def partner(df, prog1, prog2):
    idx1 = df.index(prog1)
    idx2 = df.index(prog2)
    exchange(df, idx1, idx2)
    return df


def dance(df, steps):
    for step in steps:
        if step[0] == 's':
            df = spin(df, int(step[1:]))
        elif step[0] == 'x':
            df = exchange(df, *map(int, step[1:].split('/')))
        elif step[0] == 'p':
            df = partner(df, *step[1:].split('/'))
        else:
            print("Invalid instruction", step)

    return df


if __name__ == "__main__":
    with open("input.txt") as f:
        read_instructions = f.readline().strip().split(',')

    programs = 16
    dancefloor = build_dancefloor(programs)

    dancefloor = dance(dancefloor, read_instructions)
    print("Part 1", "".join(dancefloor))

    dancefloor = build_dancefloor(programs)
    seen = []
    for i in range(1000000000):
        if "".join(dancefloor) in seen:
            # Get the last dance if we were to repeat the full 1e9 times
            # i-1 because the range() start at 1 but i needs to 0 indexed for this to work
            print(len(seen), 1000000000 % (i))
            print("Part 2", seen[1000000000 % (i)])
            print(seen)
            break
        seen.append("".join(dancefloor))

        dancefloor = dance(dancefloor, read_instructions)



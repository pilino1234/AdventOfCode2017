from collections import defaultdict


# Input grid is 25x25, we want the center to be 0,0
#    y+
# x-     x+
#    y-
def parse_infected(in_data: list):
    infected = set()

    offset = int(len(in_data) / 2)

    for num, line in enumerate(in_data):
        y_pos = offset - num
        for pos, cell in enumerate(line):
            x_pos = pos - offset
            if cell == '#':
                infected.add((x_pos, y_pos))

    return infected


def burst(infected: set, evolved=False):
    grid = defaultdict(int)

    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3

    for inf in infected:
        grid[inf] = INFECTED

    carrier_pos = (0, 0)
    carrier_dir = 0         # 0: up, 1: right, 2: down, 3: left

    directions = {
        0: (0, 1),
        1: (1, 0),
        2: (0, -1),
        3: (-1, 0)
    }

    caused_infections = 0

    for i in range(10000000 if evolved else 10000):
        # Turn carrier
        if grid[carrier_pos] == CLEAN:
            carrier_dir = (carrier_dir - 1) % 4  # turn left
            if not evolved:
                caused_infections += 1
        elif grid[carrier_pos] == INFECTED:
            carrier_dir = (carrier_dir + 1) % 4  # turn right
        elif grid[carrier_pos] == WEAKENED:
            caused_infections += 1
        elif grid[carrier_pos] == FLAGGED:
            carrier_dir = (carrier_dir + 2) % 4  # turn around

        # Update cell
        grid[carrier_pos] = (grid[carrier_pos] + (1 if evolved else 2)) % 4

        # Move carrier forward
        dir_tuple = directions[carrier_dir]
        carrier_pos = (carrier_pos[0] + dir_tuple[0], carrier_pos[1] + dir_tuple[1])

    return caused_infections


if __name__ == '__main__':
    with open("input.txt") as file:
        input_map = [line.strip() for line in file.readlines()]

    infected = parse_infected(input_map)

    print(burst(infected))
    print(burst(infected, evolved=True))

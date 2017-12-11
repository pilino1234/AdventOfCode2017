
class Hex:
    directions = {
        "n": (0, 1, -1),
        "ne": (1, 0, -1),
        "se": (1, -1, 0),
        "s": (0, -1, 1),
        "sw": (-1, 0, 1),
        "nw": (-1, 1, 0)
    }

    def __init__(self, q, r, s):
        self.q = q
        self.r = r
        self.s = s

    def neighbour(self, nb_dir):
        offsets = self.directions[nb_dir]
        return Hex(self.q + offsets[0], self.r + offsets[1], self.s + offsets[2])

    def distance(self, other):
        return (abs(self.q - other.q) + abs(self.r - other.r) + abs(self.s - other.s)) // 2

    def __repr__(self):
        return "Hex: ({q},{r},{s})".format(q=self.q, r=self.r, s=self.s)


def find_path(steps):
    hex_steps = []
    curr_pos = Hex(0, 0, 0)

    hex_steps.append(curr_pos)

    for step in steps:
        curr_pos = curr_pos.neighbour(step)
        hex_steps.append(curr_pos)

    return hex_steps


def shortest_hex_path(src, dest):
    return src.distance(dest)


def get_largest_distance_ever(path):
    dist = 0

    starting_pos = Hex(0, 0, 0)

    for step in path:
        if starting_pos.distance(step) > dist:
            dist = starting_pos.distance(step)

    return dist


if __name__ == "__main__":
    with open("input.txt") as f:
        input_dir = f.readline().strip()

    path = find_path(input_dir.split(","))

    shortest_path = shortest_hex_path(path[0], path[-1])

    print("(Part 1) Shortest distance to target", shortest_path)

    print("(Part 2) Furthest distance from source", get_largest_distance_ever(path))


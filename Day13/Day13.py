
class Layer:

    def __init__(self, depth, layer_range):
        self.range = layer_range
        self.depth = depth

    @property
    def severity(self):
        return self.range * self.depth

    def is_open(self, time):
        return time % ((self.range - 1) * 2) != 0


def create_firewall(in_layers):
    deepest_layer = int(in_layers[-1].split(": ")[0])

    fw = [None for _ in range(deepest_layer + 1)]

    for line in in_layers:
        parts = list(map(int, line.split(": ")))
        fw[parts[0]] = Layer(*parts)

    return fw


def simulate(fw, delay=0):
    sev = 0
    time = delay
    caught = False

    for layer in fw:
        if layer is not None and not layer.is_open(time):
            caught = True
            sev += layer.severity
        time += 1

    if delay > 0:
        return caught

    return sev


if __name__ == "__main__":
    with open("input.txt") as f:
        read_layers = [l.strip() for l in f]

    firewall = create_firewall(read_layers)

    severity = simulate(firewall)

    print("Part 1", severity)  # 788

    delay = 10
    while True:
        if not simulate(firewall, delay):
            break

        # if delay % 1000 == 0:
            # print("bruteforce at", delay)

        delay += 1

    print("Part 2", delay)  # 3905748

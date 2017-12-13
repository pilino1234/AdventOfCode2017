

if __name__ == "__main__":
    with open("input.txt") as f:
        read_pipes = [l.strip() for l in f]

    data = [d.split(' <-> ') for d in read_pipes]
    data = [(d[0], d[1].split(', ')) for d in data]

    # create adjacency list
    graph = {}
    for d in data:
        graph[d[0]] = d[1]

    # count the number of groups
    count = 0
    remaining = list(graph.keys())
    while remaining:
        count += 1

        root = remaining[0]
        seen = []

        queued = [root]

        while queued:
            node = queued.pop()
            if node in seen:
                continue

            if node in remaining:
                remaining.remove(node)

            seen.append(node)

            queued += [d for d in graph[node] if d not in seen]

    print(count)

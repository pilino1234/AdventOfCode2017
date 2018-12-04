
DIRECTIONS = {
    "up": (0, -1, "down"),
    "down": (0, 1, "up"),
    "left": (-1, 0, "right"),
    "right": (1, 0, "left"),
}


def lookup(maze, pos):
    try:
        return maze[pos[1]][pos[0]]
    except IndexError:
        return ""


def move(pos, dir):
    direction = DIRECTIONS[dir]
    return pos[0] + direction[0], pos[1] + direction[1]


def trace(maze):
    start_pos = maze[0].find("|")

    position = (start_pos, 0)

    found_letters = []
    last_direction = "down"

    steps = 0

    while True:
        symbol = lookup(maze, position)

        if symbol == "|":
            position = move(position, last_direction)
        elif symbol == "+":
            for i in DIRECTIONS.keys():
                if i == last_direction or last_direction == DIRECTIONS[i][2]:
                    continue
                check = move(position, i)
                if lookup(maze, check).strip():
                    position = move(position, i)
                    last_direction = i
        elif symbol == "-":
            position = move(position, last_direction)
        elif symbol.isalpha():
            found_letters.append(symbol)
            position = move(position, last_direction)
        elif symbol == " ":
            # We are done
            break
        else:
            print("Found new symbol '{}'".format(symbol))
            break

        steps += 1

    return found_letters, steps


if __name__ == '__main__':
    with open("input.txt") as f:
        read_path = [l.strip('\n') for l in f]

    sample = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
"""
    test_path = [line.strip('\n') for line in sample.split('\n')]

    letters, steps = trace(read_path)

    print("".join(letters))
    print(steps)



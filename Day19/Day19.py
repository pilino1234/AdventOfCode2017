

if __name__ == '__main__':
    with open("input.txt") as f:
        read_path = [l.strip('\n') for l in f]

    print("\n".join(read_path))



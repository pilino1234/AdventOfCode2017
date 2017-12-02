
def get_numbers(row):
    return list(map(int, row.split("\t")))


def find_divisors(input_nums):
    for idx, i in enumerate(input_nums):
        for j in input_nums[idx+1:]:
            print(i, j, i % j)
            if i % j == 0 or j % i == 0:
                return [i, j]


if __name__ == "__main__":
    with open("input.txt") as file:
        rows = file.readlines()

    print(sum(max(get_numbers(row)) - min(get_numbers(row)) for row in rows))

    print(find_divisors([5, 9, 2, 8]))

    div_sum = 0
    for row in rows:
        numbers = get_numbers(row)
        print(numbers)
        divs = find_divisors(numbers)
        divs.sort()
        div_sum += divs[1] // divs[0]

    print(div_sum)

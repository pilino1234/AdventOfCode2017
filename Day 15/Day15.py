
def generatorX(starting_value, factor, div_condition=1):
    x = starting_value
    while True:
        x *= factor
        x %= 2147483647
        if x % div_condition == 0:
            yield x


def get_lower_16b(number):
    b_number = bin(number)

    if len(b_number) > 16:
        return b_number[-16:]
    else:
        return format(number, '016b')


genA = generatorX(634, 16807)
# genA = generatorX(65, 16807)  # Puzzle test case

genB = generatorX(301, 48271)
# genB = generatorX(8921, 48271)  # Puzzle test case

judge_count = 0
for i in range(int(4e7)):
    if i % 10000 == 0:
        print("generator step", i)

    if get_lower_16b(next(genA)) == get_lower_16b(next(genB)):
        judge_count += 1

print("Part 1:", judge_count)


genA = generatorX(634, 16807, 4)
# genA = generatorX(65, 16807, 4)  # Puzzle test case

genB = generatorX(301, 48271, 8)
# genB = generatorX(8921, 48271, 8)  # Puzzle test case

impatient_judge_count = 0
for i in range(int(5e6)):
    if i % 10000 == 0:
        print("generator2 step", i)

    if get_lower_16b(next(genA)) == get_lower_16b(next(genB)):
        impatient_judge_count += 1

print("Part 2:", impatient_judge_count)


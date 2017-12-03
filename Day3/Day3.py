import math


def largest_ring_size(number):
    size = math.ceil(math.sqrt(number))
    size = size if size % 2 != 0 else size + 1
    return size


def manhattan_distance_to_center(number):
    ring_side_length = largest_ring_size(number)

    steps_to_centre_from_ring_axis = (ring_side_length - 1) // 2

    axes_numbers = [ring_side_length ** 2 - ((ring_side_length - 1) * i) - ring_side_length // 2 for i in range(0, 4)]

    steps_to_ring_axis_from_number = min([abs(axis_number - number) for axis_number in axes_numbers])

    result = steps_to_centre_from_ring_axis + steps_to_ring_axis_from_number
    return result


if __name__ == "__main__":
    input_number = 368078

    # part 1
    print(manhattan_distance_to_center(input_number))

    # part 2 from spreadsheet
    print(369601)

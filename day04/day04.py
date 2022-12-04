def part1(input):
    num_containing_ranges = 0
    for line in input:
        [first_range, second_range] = line.strip().split(",")
        [first_range_start, first_range_stop] = list(map(int, first_range.split("-")))
        [second_range_start, second_range_stop] = list(map(int, second_range.split("-")))
        if (
            first_range_start <= second_range_start
            and first_range_stop >= second_range_stop
        ) or (
            first_range_start >= second_range_start
            and first_range_stop <= second_range_stop
        ):
            num_containing_ranges += 1
    return num_containing_ranges


def part2(input):
    num_overlapping_ranges = 0
    for line in input:
        [first_range, second_range] = line.strip().split(",")
        first_range = list(map(int, first_range.split("-")))
        second_range = list(map(int, second_range.split("-")))
        overlaps = False
        for range_delim in first_range:
            if second_range[0] <= range_delim <= second_range[1]:
                overlaps = True
        for range_delim in second_range:
            if first_range[0] <= range_delim <= first_range[1]:
                overlaps = True

        if overlaps:
            num_overlapping_ranges += 1

    return num_overlapping_ranges


TEST_INPUT = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8",
]


def test_part1():
    assert part1(TEST_INPUT) == 2


def test_part2():
    assert part2(TEST_INPUT) == 4


if __name__ == "__main__":
    with open("day04/puzzle_input.txt") as puzzle_input:
        lines = puzzle_input.readlines()
        print(part1(lines.copy()))
        print(part2(lines.copy()))

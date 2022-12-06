from functools import reduce


def find_marker(num_symbols):
    def _find_marker(sequence):
        for i in range(num_symbols, len(sequence)):
            if reduce(
                lambda x, y: x and y,
                [
                    sequence[j] != sequence[k]
                    for j in range(i - num_symbols, i)
                    for k in range(i - num_symbols, i)
                    if j != k
                ],
            ):
                return i
    return _find_marker


part1 = find_marker(4)


part2 = find_marker(14)


TEST_DATA = {
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb": (7, 19),
    "bvwbjplbgvbhsrlpgdmjqwftvncz": (5, 23),
    "nppdvjthqldpwncqszvftbrmjlhg": (6, 23),
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": (10, 29),
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": (11, 26),
}


def test_part1():
    for i, (e, _) in TEST_DATA.items():
        assert part1(i) == e


def test_part2():
    for i, (_, e) in TEST_DATA.items():
        assert part2(i) == e


if __name__ == "__main__":
    with open("day06/puzzle_input.txt") as puzzle_input:
        line = puzzle_input.readline()
        print(part1(line))
        print(part2(line))

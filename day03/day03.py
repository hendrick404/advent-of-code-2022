def priority(c: str):
    return ord(c) - 38 if c.isupper() else ord(c) - 96


def part1(lines):
    priority_sum = 0
    for line in lines:
        for i in {x for x in line[: len(line) // 2] if x in line[len(line) // 2 :]}:
            priority_sum += priority(i)
    return priority_sum

def part2(lines):
    badge_priority_sum = 0
    for i in range(0,len(lines),3):
        badge = {x for x in lines[i].strip() if x in lines[i+1].strip() and x in lines[i+2].strip()}
        assert len(badge) == 1
        badge_priority_sum += sum(map(priority, badge))
    return badge_priority_sum


TEST_INPUT = [
    "vJrwpWtwJgWrhcsFMMfFFhFp\n",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\n",
    "PmmdzqPrVvPwwTWBwg\n",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\n",
    "ttgJtRGJQctTZtZT\n",
    "CrZsJsPPZsGzwwsLwLmpwMDw",
]


def test_part1():
    assert part1(TEST_INPUT) == 157


def test_part2():
    assert part2(TEST_INPUT) == 70


if __name__ == "__main__":
    with open("day03/puzzle_input.txt") as file:
        puzzle_input = file.readlines()
        print(part1(puzzle_input.copy()))
        print(part2(puzzle_input.copy()))
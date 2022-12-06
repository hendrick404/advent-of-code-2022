from collections import deque


def parse_input(input, num_stacks):
    stacks = [deque() for _ in range(num_stacks + 1)]
    instructions = []
    for line in input:
        if line.startswith("move"):
            instruction = list(map(str.strip, line.split(" ")))
            assert instruction[0] == "move"
            assert instruction[2] == "from"
            assert instruction[4] == "to"
            instructions.append(
                (int(instruction[1]), int(instruction[3]), int(instruction[5]))
            )
        else:
            crates = [line[i : i + 4].strip() for i in range(0, len(line), 4)]
            for (i, c) in enumerate(crates):
                if c and c.startswith("["):
                    stacks[i + 1].appendleft(c[1])
    return stacks, instructions


def part1(input, num):
    stacks, instructions = parse_input(input, num)
    for num_crates, from_stack, to_stack in instructions:
        for _ in range(num_crates):
            stacks[to_stack].append(stacks[from_stack].pop())
    res = ""
    for i in range(1, num+1):
        res += stacks[i].pop()
    return res


def part2(input, num):
    stacks, instructions = parse_input(input, num)
    for num_crates, from_stack, to_stack in instructions:
        crates = deque()
        for _ in range(num_crates):
            crates.appendleft(stacks[from_stack].pop())
        for crate in crates:
            stacks[to_stack].append(crate)
    res = ""
    for i in range(1, num+1):
        res += stacks[i].pop()
    return res    

TEST_INPUT = [
    "    [D]    ",
    "[N] [C]    ",
    "[Z] [M] [P]",
    " 1   2   3 ",
    "move 1 from 2 to 1",
    "move 3 from 1 to 3",
    "move 2 from 2 to 1",
    "move 1 from 1 to 2",
]


def test_part1():
    assert part1(TEST_INPUT, 3) == "CMZ"


def test_part2():
    assert part2(TEST_INPUT,3) == "MCD"


if __name__ == "__main__":
    with open("day05/puzzle_input.txt") as puzzle_input:
        lines = puzzle_input.readlines()
        print(part1(lines.copy(), 9))
        print(part2(lines.copy(), 9))
def part1(input) -> int:
    score = 0
    for line in input:
        line = line.strip()
        actions = line.split(" ")
        elf_action = actions[0]
        own_action = actions[1]
        if own_action == "X":
            score += 1
            if elf_action == "A":
                score += 3
            elif elf_action == "C":
                score += 6
        elif own_action == "Y":
            score += 2
            if elf_action == "B":
                score += 3
            elif elf_action == "A":
                score += 6
        elif own_action == "Z":
            score += 3
            if elf_action == "C":
                score += 3
            elif elf_action == "B":
                score += 6
    return score

def part2(input):
    table = {
        # Lose so choose scissors
        ("A","X"): 3,
        # Draw so choose rock
        ("A","Y"): 1,
        # Win so choose paper
        ("A","Z"): 2,
        # Lose so choose rock
        ("B","X"): 1,
        # Draw so choose paper
        ("B","Y"): 2,
        # Win so choose scissors
        ("B","Z"): 3,
        # Lose so choose paper
        ("C","X"): 2,
        # Draw so choose scissors
        ("C","Y"): 3,
        # Win so choose rock
        ("C","Z"): 1,
    }
    score = 0
    for line in input:
        line = line.strip()
        actions = line.split(" ")
        elf_action = actions[0]
        outcome = actions[1]
        if outcome == "X":
            score += table[elf_action, outcome]
        elif outcome == "Y":
            score += table[elf_action, outcome] + 3
        elif outcome == "Z":
            score += table[elf_action, outcome] + 6
    return score

def test_part1():
    test_input = ["A Y\n","B X\n","C Z"]
    assert part1(test_input) == 15

def test_part2():
    test_input = ["A Y\n","B X\n","C Z"]
    assert part2(test_input) == 12


if __name__ == "__main__":
    with open("day02/puzzle_input.txt") as file:
        lines = file.readlines()
        print(part1(lines.copy()))
        print(part2(lines.copy()))
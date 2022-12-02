with open("puzzle_input") as puzzle_input:
    lines = puzzle_input.readlines()
    sums = []
    sub_sum = 0
    for l in lines:
        if l == "\n":
            sums.append(sub_sum)
            sub_sum = 0
        else:
            sub_sum += int(l)
    print(max(sums))
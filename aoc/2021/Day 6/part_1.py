# Advent of code 2021 : Day 6 | Part 1

# Author = Abhinav
# Date = 6th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/6)

# Solution :

from collections import defaultdict, Counter

inputs = Counter([int(x) for x in open('aoc/2021/Day 6/input.txt').read().strip().split(',')])


def solve(S, n):
    inputs = S
    for day in range(n):
        input = defaultdict(int)
        for x, cnt in inputs.items():
            if x == 0:
                input[6] += cnt
                input[8] += cnt
            else:
                input[x-1] += cnt
        inputs = input
    return sum(inputs.values())


print(solve(inputs, 80))


# Answer : 351188

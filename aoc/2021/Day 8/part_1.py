# Advent of code 2021 : Day 8 | Part 1

# Author = Abhinav
# Date = 8th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/8)

# Solution :

inputs = open("aoc/2021/Day 8/input.txt")
inputs = inputs.read().splitlines()

result = 0

for line in inputs:
    _, output = line.split(" | ")
    output = output.split()

    result += sum(len(_) in (2, 3, 4, 7) for _ in output)

print(result)

# Answer : 255

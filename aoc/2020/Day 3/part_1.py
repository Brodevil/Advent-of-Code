# Advent of code 2021 : Day 3 | Part 1
# Source : https://adventofcode.com/2020/day/3


infile = "aoc/2020/Day 3/input.txt"
inputs = open(infile).read().splitlines()

trees = 0
x, y = len(inputs[0]), len(inputs)
X, Y = 0, 0
right = True

for _ in range(x):
    if right:
        X += 3
    Y += 1
    if inputs[Y][X] == "#":
        trees += 1

print(trees)

# Answer : 

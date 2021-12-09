# Advent of code 2021 : Day 1 | Part 2
# Source : https://adventofcode.com/2020/day/1

infile = "aoc/2020/Day 1/input.txt"
inputs = list(map(int, open(infile).read().splitlines()))

print([i*j*_ for i in inputs for j in inputs for _ in inputs if i + j + _ == 2020][0])

# Answer : 165080960

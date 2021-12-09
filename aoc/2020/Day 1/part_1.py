# Advent of code 2021 : Day 1 | Part 1
# Source : https://adventofcode.com/2020/day/1

infile = "aoc/2020/Day 1/input.txt"
inputs = list(map(int, open(infile).read().splitlines()))

print([i * _ for _ in inputs for i in inputs if _ + i == 2020][0])

# Answer : 157059
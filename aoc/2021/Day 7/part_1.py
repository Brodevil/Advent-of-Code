# Advent of code 2021 : Day 7 | Part 1

# Author = Abhinav
# Date = 7th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/7)

# Solution : 

inputs = open("aoc/2021/Day 7/input.txt")
inputs = list(map(int, inputs.read().split(",")))

real = list()

for _ in range(min(inputs), max(inputs)+1):
    ls = list()
    for i in inputs:
        ls.append(abs(i-_))
    real.append(sum(ls))

print(min(real))

# Answer : 331067

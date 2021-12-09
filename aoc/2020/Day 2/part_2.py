# Advent of code 2021 : Day 2 | Part 1
# Source : https://adventofcode.com/2020/day/2

infile = "aoc/2020/Day 2/input.txt"
inputs = open(infile).read().splitlines()

total = 0

for _ in inputs:
    _ = _.split()
    word, letter = _[2], _[1][0]
    lo, hi = map(int, _[0].split('-'))

    c = word.count(letter)

    if (word[lo-1]==letter) ^ (word[hi-1]==letter):
        total += 1

print(total)

# Answer : 251
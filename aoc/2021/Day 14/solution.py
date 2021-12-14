# Advent of code 2021 : Day 14 | Part 1 & Part 2

# Author = Abhinav
# Date = 14th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/14)

# Solution :

from collections import Counter

infile = "aoc/2021/Day 14/input.txt"
S, rules = open(infile).read().split("\n\n")

R = {}
for line in rules.strip().split("\n"):
    start, end = line.strip().split(" -> ")
    R[start] = end


C1 = Counter()

for i in range(len(S) - 1):
    C1[S[i] + S[i + 1]] += 1

for t in range(41):
    if t in [10, 40]:
        CF = Counter()
        
        for k in C1:
            CF[k[0]] += C1[k]
        CF[S[-1]] += 1
        print(max(CF.values()) - min(CF.values()))

    C2 = Counter()
    
    for k in C1:
        C2[k[0] + R[k]] += C1[k]
        C2[R[k] + k[1]] += C1[k]
    C1 = C2


# Answer : Part 1 = 3697 | Part 2 = 4371307836157

# Advent of code 2021 : Day 3 | Part 1
# Source : https://adventofcode.com/2020/day/23

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

G = []
infile = "aoc/2020/Day 3/input.txt"
G = open(infile).read().splitlines()

ans = 1
for (dc,dr) in slopes:
    r = 0
    c = 0 
    score = 0
    while r < len(G):
        c += dc
        r += dr
        if r<len(G) and G[r][c%len(G[r])]=='#':
            score += 1
    ans *= score
    if dc==3 and dr==1:
        print(score)
print(ans)

# Answer : 
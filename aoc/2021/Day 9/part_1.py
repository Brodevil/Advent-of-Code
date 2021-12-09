# Advent of code 2021 : Day 9 | Part 1

# Author = Abhinav
# Date = 9th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/9)

# Solution :


file = "aoc/2021/Day 9/input.txt"
G = []
for line in open(file):
    G.append([int(x) for x in list(line.strip())])

R = len(G)
C = len(G[0])

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]
ans = 0

for r in range(R):
    for c in range(C):
        ok = True
        for d in range(4):
            rr = r + DR[d]
            cc = c + DC[d]
            if 0 <= rr < R and 0 <= cc < C and G[rr][cc] <= G[r][c]:
                ok = False
        if ok:
            ans += G[r][c] + 1

print(ans)

# Answer : 575

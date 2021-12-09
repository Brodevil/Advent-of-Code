# Advent of code 2021 : Day 9 | Part 2

# Author = Abhinav
# Date = 9th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/9)

# Solution : 

from collections import deque

file = "aoc/2021/Day 9/input.txt"
G = list()

for line in open(file):
    G.append([int(x) for x in list(line.strip())])

R = len(G)
C = len(G[0])

DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]

S = []
SEEN = set()

for r in range(R):
    for c in range(C):
        if (r, c) not in SEEN and G[r][c] != 9:
            size = 0
            Q = deque()
            Q.append((r, c))
            
            while Q:
                (r, c) = Q.popleft()
                if (r, c) in SEEN:
                    continue
                SEEN.add((r, c))
                size += 1
                for d in range(4):
                    rr = r+DR[d]
                    cc = c+DC[d]
                    if 0 <= rr < R and 0 <= cc < C and G[rr][cc] != 9:
                        Q.append((rr, cc))
            
            S.append(size)


S.sort()
print(S[-1]*S[-2]*S[-3])


# Answer : 1019700

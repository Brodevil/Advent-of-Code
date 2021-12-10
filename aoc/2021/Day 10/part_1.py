# Advent of code 2021 : Day 10 | Part 1

# Author = Abhinav
# Date = 10th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/10)

# Solution :

from collections import deque

SCORES = []
ans = 0
infile = "aoc/2021/Day 10/input.txt"

for line in open(infile):
    bad = False
    S = deque()
    
    for c in line.strip():
        if c in ["(", "[", "{", "<"]:
            S.append(c)
        
        elif c == ")":
            if S[-1] != "(":
                ans += 3
                bad = True
                break
            else:
                S.pop()
        
        elif c == "]":
            if S[-1] != "[":
                ans += 57
                bad = True
                break
            else:
                S.pop()
        
        elif c == "}":
            if S[-1] != "{":
                ans += 1197
                bad = True
                break
            else:
                S.pop()
        
        elif c == ">":
            if S[-1] != "<":
                ans += 25137
                bad = True
                break
            else:
                S.pop()
    
    if not bad:
        score = 0
        P = {"(": 1, "[": 2, "{": 3, "<": 4}
        
        for c in reversed(S):
            score = score * 5 + P[c]
        SCORES.append(score)

print(ans)

# Answer : 462693

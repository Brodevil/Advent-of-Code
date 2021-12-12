# Advent of code 2021 : Day 12 | Part 1 & Part 2

# Author = Abhinav
# Date = 12th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/12)

# Solution :

infile = "aoc/2021/Day 12/input.txt"

from collections import defaultdict, deque

ls = defaultdict(list)
for line in open(infile):
    a, b = line.strip().split("-")
    ls[a].append(b)
    ls[b].append(a)


def solve(p1):
    start = ("start", set(["start"]), None)
    ans = 0
    Q = deque([start])
    
    while Q:
        pos, small, twice = Q.popleft()
        if pos == "end":
            ans += 1
            continue
        
        for y in ls[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small, twice))
            
            elif y in small and twice is None and y not in ["start", "end"] and not p1:
                Q.append((y, small, y))
    return ans


print(solve(p1=True))
print(solve(p1=False))

# Answer : Part 1 - 3887 | Part 2 - 102834

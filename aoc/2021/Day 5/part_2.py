# Advent of code 2021 : Day 4 | Part 2

# Author = Abhinav
# Date = 4th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/4)

# Solution : 

# Advent of code 2021 : Day 5 | Part 1

# Author = Abhinav
# Date = 5th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/5)

# Solution : 

from collections import defaultdict

ls = defaultdict(int)

for line in open("input.txt", "rt"):
    start,end = line.split('->')
    x1,y1 = start.split(',')
    x2,y2 = end.split(',')
    
    x1 = int(x1.strip())
    y1 = int(y1.strip())
    x2 = int(x2.strip())
    y2 = int(y2.strip())

    dx = x2-x1
    dy = y2-y1

    for i in range(1+max(abs(dx),abs(dy))):
        x = x1+(1 if dx>0 else (-1 if dx<0 else 0))*i
        y = y1+(1 if dy>0 else (-1 if dy<0 else 0))*i
        ls[(x,y)] += 1

print(len([k for k in ls if ls[k]>1]))


# Answer : 19939

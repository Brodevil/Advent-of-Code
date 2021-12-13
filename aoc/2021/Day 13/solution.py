# Advent of code 2021 : Day 13 | Part 1 & Part 2

# Author = Abhinav
# Date = 13th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/13)

# Solution :

infile = 'aoc/2021/Day 13/input.txt'

did_p1 = False
G = {}

for line in open(infile):
    line = line.strip()
    
    if line and line.startswith('fold'):
        G2 = {}
        instr = line.split()[-1]
        d,v = instr.split('=')
        v = int(v)
        
        if d == 'x':
            for (x,y) in G:
                if x < v:
                    G2[(x,y)] = True
                else:
                    G2[(v-(x-v), y)] = True
        
        else:
            assert d == 'y'
            for (x,y) in G:
                if y < v:
                    G2[(x,y)] = True
                else:
                    G2[(x, v-(y-v))] = True
        G = G2
        if not did_p1:
            did_p1 = True
            print(len(G2))
    
    elif line:
        x,y = [int(v) for v in line.strip().split(',')]
        G[(x,y)] = True


X = max([x for x,y in G.keys()])
Y = max([y for x,y in G.keys()])

solution = ''
for y in range(Y+1):
    for x in range(X+1):
        solution += ('x' if (x,y) in G else ' ')
    print(solution)
    solution = ""

# Answer : Part 1 - 827 | Part 2 ; EAHKRECP

# Advent of code 2021 : Day 11 | Part 1 & Part 2

# Author = Abhinav
# Date = 11th of December 2021
# Source =  [Advent Of Code](https://adventofcode.com/2021/day/11)

# Solution :

infile = "aoc/2021/Day 11/input.txt"

inputs = []
for line in open(infile):
    inputs.append([int(x) for x in line.strip()])


R = len(inputs)
C = len(inputs[0])

ans = 0


def flash(r, c):
    global ans
    ans += 1
    inputs[r][c] = -1

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            rr = r + dr
            cc = c + dc
            
            if 0 <= rr < R and 0 <= cc < C and inputs[rr][cc] != -1:
                inputs[rr][cc] += 1
                if inputs[rr][cc] >= 10:
                    flash(rr, cc)


t = 0
while True:
    t += 1
    for r in range(R):
        for c in range(C):
            inputs[r][c] += 1
    
    for r in range(R):
        for c in range(C):
            if inputs[r][c] == 10:
                flash(r, c)
    done = True
    
    for r in range(R):
        for c in range(C):
            if inputs[r][c] == -1:
                inputs[r][c] = 0
            else:
                done = False
    
    if t == 100:
        print(ans)
    if done:
        print(t)
        break


# Answer : Part 1 - 1647 | Part 2 - 348

import itertools
import functools
import math
import collections
import sys

with open(sys.argv[1], 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

start = None

for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == 'S':
            start = (i, j)
            break
    if start is not None: break

print('Start is', start)

def next_index(curr, prev):
    cc = lines[curr[0]][curr[1]]
    poss = []
    match cc:
        case '-':
            poss = [(curr[0], curr[1]+1),(curr[0], curr[1]-1)] 
        case '|':
            poss = [(curr[0]+1, curr[1]),(curr[0]-1, curr[1])] 
        case '7':
            poss = [(curr[0], curr[1]-1),(curr[0]+1, curr[1])] 
        case 'J':
            poss = [(curr[0], curr[1]-1),(curr[0]-1, curr[1])] 
        case 'L':
            poss = [(curr[0], curr[1]+1),(curr[0]-1, curr[1])] 
        case 'F':
            poss = [(curr[0], curr[1]+1),(curr[0]+1, curr[1])] 
        case 'S':
            print('reached S')
            return None
        case '.':
            raise ValueError('Reached non pipe')
    if prev == poss[0]: return poss[1]
    return poss[0]

curr = (start[0], start[1]+1)
prev = start
idx = [start, curr]

while (nx := next_index(curr, prev)) is not None:
    prev, curr = curr, nx
    idx.append(curr)

idx.pop()

print('Length of idx', len(idx))
n = len(lines)
m = len(lines[0])

grid = [[' '] * m for _ in range(n)]
for i, j in idx:
    grid[i][j] = lines[i][j]

grid[start[0]][start[1]] = sys.argv[2]

for i in range(n):
    print(''.join(grid[i]))

ans = 0
for row in grid:
    inside = 0
    corners = []
    for c in row:
        match c:
            case '|':
                if corners:
                    corners.pop()
                else:
                    corners.append(c)
            case 'L':
                if corners and corners[-1] == 'J':
                    corners.pop()
                else:
                    corners.append(c)
            case 'J':
                if corners and corners[-1] == 'L':
                    corners.pop()
                elif corners and corners[-1] == 'F':
                    corners.pop()
                    if corners: corners.pop()
                    else: corners.append('|')
                else:
                    corners.append(c)
            case 'F':
                if corners and corners[-1] == '7':
                    corners.pop()
                else:
                    corners.append(c)
            case '7':
                if corners and corners[-1] == 'F':
                    corners.pop()
                elif corners and corners[-1] == 'L':
                    corners.pop()
                    if corners: corners.pop()
                    else: corners.append('|')
                else:
                    corners.append(c)
            case ' ':
                ans += len(corners) % 2
    print('current ans', ans)

print(ans)

# free - 5576


import itertools
import functools
import math
import collections

with open('input.txt', 'r') as f:
    lines = [list(line.strip()) for line in f.readlines()]

start = None
dist = collections.defaultdict(lambda: float('inf'))

for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == 'S':
            start = (i, j)
            break
    if start is not None: break

print(start)
prev = start
dist[start] = 0
steps = 0

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

curr = (start[0], start[1]-1)
dist[curr] = 1
steps = 2

while (nx := next_index(curr, prev)) is not None:
    prev, curr = curr, nx
    dist[curr] = min(dist[curr], steps)
    steps += 1

curr = (start[0], start[1]+1)
dist[curr] = 1
steps = 2

while (nx := next_index(curr, prev)) is not None:
    prev, curr = curr, nx
    dist[curr] = min(dist[curr], steps)
    steps += 1
    

print(max(dist.values()))



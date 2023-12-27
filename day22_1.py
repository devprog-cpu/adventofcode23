import itertools
import functools
import math
import collections
import sys
import operator
import heapq
import sys
import tracemalloc

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

bricks = []
lx, ly = 0, 0
for line in lines:
    ends = line.split('~')
    s = tuple(int(x) for x in ends[0].split(','))
    e = tuple(int(x) for x in ends[1].split(','))
    bricks.append((s, e))
    if s[0] > e[0] or s[1] > e[1] or s[2] > e[2]:
        raise ValueError('reversed pair')
    lx = max(lx, s[0], e[0])
    ly = max(ly, s[1], e[1])

bricks.sort(key = lambda b: b[0][2])
num_bricks = len(bricks)
lx += 1
ly += 1
# print('lengths', num_bricks, lx, ly)

state = [[(0, 0)] * ly for _ in range(lx)]
supported_by = [set() for _ in range(num_bricks + 1)]

for index, brick in enumerate(bricks, start = 1):
    start, end = brick
    startx, starty, startz = start
    endx, endy, endz = end

    if endx != startx:
        curr_height = 0
        top_bricks = []
        sy = starty
        for i in range(startx, endx + 1):
            if state[i][sy][1] > curr_height:
                top_bricks = []
                curr_height = state[i][sy][1]
            if state[i][sy][1] == curr_height:
                top_bricks.append(state[i][sy][0])
        for b in top_bricks:
            supported_by[index].add(b)
        new_height = curr_height + 1
        for i in range(startx, endx + 1):
            state[i][sy] = (index, new_height)
    elif endy != starty:
        curr_height = 0
        top_bricks = []
        sx = startx
        for i in range(starty, endy + 1):
            if state[sx][i][1] > curr_height:
                top_bricks = []
                curr_height = state[sx][i][1]
            if state[sx][i][1] == curr_height:
                top_bricks.append(state[sx][i][0])
        for b in top_bricks:
            supported_by[index].add(b)
        new_height = curr_height + 1
        for i in range(starty, endy + 1):
            state[sx][i] = (index, new_height)
    else:
        sx, sy = startx, starty
        curr = state[sx][sy]
        supported_by[index].add(curr[0])
        new_height = curr[1] + endz - startz + 1
        state[sx][sy] = (index, new_height)

# print(supported_by)
necessary = set()
for b in supported_by:
    if len(b) == 1:
        necessary.update(b)
necessary.discard(0)
# print(necessary)
print(num_bricks - len(necessary))




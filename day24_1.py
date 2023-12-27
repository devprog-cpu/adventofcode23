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

n = len(lines)
stones = []
for line in lines:
    sp = line.split(' @ ')
    pos = tuple(int(x) for x in sp[0].split(', '))
    vel = tuple(int(x) for x in sp[1].split(', '))
    stones.append((pos, vel))

'''
for intersection -
y = slope1 * (x - x1) + y1
y = slope2 * (x - x2) + y2

slope1 * (x - x1) + y1 = slope2 * (x - x2) + y2
(slope1 - slope2) * x = (slope1 * x1) - (slope2 * x2) + (y2 - y1)

x = ((slope1 * x1) - (slope2 * x2) + (y2 - y1))  / (slope1 - slope2)
'''

def distance(x1, y1, x2, y2):
    yd = y2 - y1
    xd = x2 - x1
    return math.sqrt(yd ** 2 + xd ** 2)

minp, maxp = 200000000000000, 400000000000000
# minp, maxp = 7, 27

ans = 0

for i in range(n):
    slope1 = stones[i][1][1] / stones[i][1][0]
    x1, y1 = stones[i][0][0], stones[i][0][1]
    for j in range(i + 1, n):
        # print('Checking stone', stones[i], stones[j])
        slope2 = stones[j][1][1] / stones[j][1][0]
        x2, y2 = stones[j][0][0], stones[j][0][1]

        # print('slopes', slope1, slope2)
        if slope1 == slope2: continue

        x = ((slope1 * x1) - (slope2 * x2) + (y2 - y1)) / (slope1 - slope2)
        y = slope1 * (x - x1) + y1

        if not(minp <= x <= maxp and minp <= y <= maxp): continue

        x3, y3 = x1 + stones[i][1][0], y1 + stones[i][1][1]
        x4, y4 = x2 + stones[j][1][0], y2 + stones[j][1][1]
        if distance(x, y, x1, y1) > distance(x, y, x3, y3) and distance(x, y, x2, y2) > distance(x, y, x4, y4): 
            ans += 1

print(ans)


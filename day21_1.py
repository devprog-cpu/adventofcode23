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

m = len(lines)
n = len(lines[0])

sx, sy = 0, 0

for i, line in enumerate(lines):
    if 'S' in line:
        sx = i
        sy = line.index('S')
        lines[i] = line.replace('S', '.')
        break
    
q = set()
q.add((sx, sy))
steps = 64

while steps > 0:
    nq = set()
    while q:
        cx, cy = q.pop()
        if cx - 1 >= 0 and lines[cx-1][cy] == '.':
            nq.add((cx-1, cy))
        if cx + 1 < m and lines[cx+1][cy] == '.':
            nq.add((cx+1, cy))
        if cy - 1 >= 0 and lines[cx][cy-1] == '.':
            nq.add((cx, cy-1))
        if cy + 1 < n and lines[cx][cy+1] == '.':
            nq.add((cx, cy+1))
    q = nq
    steps -= 1

print(len(q))

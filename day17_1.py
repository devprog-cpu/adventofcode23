import itertools
import functools
import math
import collections
import sys
import operator
import heapq

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]


U, D, L, R = 'U', 'D', 'L', 'R'
m = len(lines)
n = len(lines[0])
grid = [[int(lines[i][j]) for j in range(n)] for i in range(m)]

mincost = [[collections.defaultdict(lambda: float('inf')) for j in range(n)] for _ in range(m)]
q = [(0, 0, 0, 0, 'X')] # cost, x, y, steps, drc

while q:
    cost, x, y, steps, drc = heapq.heappop(q)
    if (steps < 3 or drc != U) and drc != D and x-1 >= 0 and cost + grid[x-1][y] < mincost[x-1][y][(1 if drc != U else steps + 1, U)]:
        heapq.heappush(q, ( cost + grid[x-1][y], x-1, y, 1 if drc != U else steps + 1, U ) )
        mincost[x-1][y][(1 if drc != U else steps + 1, U)] = cost + grid[x-1][y]
    if (steps < 3 or drc != D) and drc != U and x+1 < m and cost + grid[x+1][y] < mincost[x+1][y][(1 if drc != D else steps + 1, D)]:
        heapq.heappush(q, ( cost + grid[x+1][y], x+1, y, 1 if drc != D else steps + 1, D ) )
        mincost[x+1][y][(1 if drc != D else steps + 1, D)] = cost + grid[x+1][y]
    if (steps < 3 or drc != L) and drc != R and y - 1 >= 0 and cost + grid[x][y-1] < mincost[x][y-1][(1 if drc != L else steps + 1, L)]:
        heapq.heappush(q, ( cost + grid[x][y-1], x, y-1, 1 if drc != L else steps + 1, L ) )
        mincost[x][y-1][(1 if drc != L else steps + 1, L)] = cost + grid[x][y-1]
    if (steps < 3 or drc != R) and drc != L and y + 1 < n and cost + grid[x][y+1] < mincost[x][y+1][(1 if drc != R else steps + 1, R)]:
        heapq.heappush(q, ( cost + grid[x][y+1], x, y+1, 1 if drc != R else steps + 1, R ) )
        mincost[x][y+1][(1 if drc != R else steps + 1, R)] = cost + grid[x][y+1]

print(min(mincost[m-1][n-1].values()))


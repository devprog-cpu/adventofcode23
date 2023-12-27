import itertools
import functools
import math
import collections
import sys
import operator
import heapq

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

mn, mx = 4, 10 

U, D, L, R = 'U', 'D', 'L', 'R'
m = len(lines)
n = len(lines[0])
grid = [[int(lines[i][j]) for j in range(n)] for i in range(m)]

mincost = [[collections.defaultdict(lambda: float('inf')) for j in range(n)] for _ in range(m)]
q = [(0, 0, 0, 0, R), (0, 0, 0, 0, D)] # cost, x, y, steps, drc

while q:
    # print(q)
    cost, x, y, steps, drc = heapq.heappop(q)
    c1, c2 = cost, cost 
    if drc == U or drc == D:
        for i in range(1, mn):
            c1 += grid[x][y-i] if y-i >= 0 else 0
            c2 += grid[x][y+i] if y+i < n else 0
        for i in range(mn, mx+1):
            if y - i >= 0:
                c1 += grid[x][y-i]
                # print('c1 after adding', c1, L)
                if c1 < mincost[x][y-i][(i, L)]:
                    heapq.heappush(q, (c1, x, y-i, i, L))
                    mincost[x][y-i][(i, L)] = c1
            if y + i < n:
                c2 += grid[x][y+i]
                # print('c2 after adding', c2, R)
                if c2 < mincost[x][y+i][(i, R)]:
                    heapq.heappush(q, (c2, x, y+i, i, R))
                    mincost[x][y+i][(i, R)] = c2
    else:
        for i in range(1, mn):
            c1 += grid[x-i][y] if x-i >= 0 else 0
            c2 += grid[x+i][y] if x+i < m else 0
        for i in range(mn, mx+1):
            if x - i >= 0:
                c1 += grid[x-i][y]
                # print('c1 after adding', c1, U)
                if c1 < mincost[x-i][y][(i, U)]:
                    heapq.heappush(q, (c1, x-i, y, i, U))
                    mincost[x-i][y][(i, U)] = c1
            if x + i < m:
                c2 += grid[x+i][y]
                # print('c2 after adding', c2, D)
                if c2 < mincost[x+i][y][(i, D)]:
                    heapq.heappush(q, (c2, x+i, y, i, D))
                    mincost[x+i][y][(i, D)] = c2
        

    # if (steps < mx or drc != U) and drc != D and x-1 >= 0 and cost + grid[x-1][y] < mincost[x-1][y][(1 if drc != U else steps + 1, U)]:
    #     heapq.heappush(q, ( cost + grid[x-1][y], x-1, y, 1 if drc != U else steps + 1, U ) )
    #     mincost[x-1][y][(1 if drc != U else steps + 1, U)] = cost + grid[x-1][y]
    # if (steps < mx or drc != D) and drc != U and x+1 < m and cost + grid[x+1][y] < mincost[x+1][y][(1 if drc != D else steps + 1, D)]:
    #     heapq.heappush(q, ( cost + grid[x+1][y], x+1, y, 1 if drc != D else steps + 1, D ) )
    #     mincost[x+1][y][(1 if drc != D else steps + 1, D)] = cost + grid[x+1][y]
    # if (steps < mx or drc != L) and drc != R and y - 1 >= 0 and cost + grid[x][y-1] < mincost[x][y-1][(1 if drc != L else steps + 1, L)]:
    #     heapq.heappush(q, ( cost + grid[x][y-1], x, y-1, 1 if drc != L else steps + 1, L ) )
    #     mincost[x][y-1][(1 if drc != L else steps + 1, L)] = cost + grid[x][y-1]
    # if (steps < mx or drc != R) and drc != L and y + 1 < n and cost + grid[x][y+1] < mincost[x][y+1][(1 if drc != R else steps + 1, R)]:
    #     heapq.heappush(q, ( cost + grid[x][y+1], x, y+1, 1 if drc != R else steps + 1, R ) )
    #     mincost[x][y+1][(1 if drc != R else steps + 1, R)] = cost + grid[x][y+1]

print(min(mincost[m-1][n-1].values()))


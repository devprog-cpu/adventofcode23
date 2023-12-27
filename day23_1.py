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

sys.setrecursionlimit(20000)
m = len(lines)
n = len(lines[0])

visited = [[False] * n for _ in range(m)]
directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}

longest_found = 0

def longest_path(i, j, steps):
    # print('Called', i, j, steps)
    if i == m - 1:
        global longest_found
        longest_found = max(longest_found, steps)
        return
    visited[i][j] = True
    for di, dj in directions:
        ni = i + di
        nj = j + dj
        ns = steps + 1
        moving = True
        while True:
            # print('On', ni, nj)
            if ni < 0 or ni >= m or nj < 0 or nj >= n:
                moving = False
                break
            if lines[ni][nj] == '#' or visited[ni][nj]:
                moving = False
                break
            if lines[ni][nj] == '.':
                break
            match lines[ni][nj]:
                case '>':
                    nj += 1
                    ns += 1
                case '<':
                    nj -= 1
                    ns += 1
                case 'v':
                    ni += 1
                    ns += 1
                case '^':
                    ni -= 1
                    ns += 1
        if moving:
            longest_path(ni, nj, ns)
    visited[i][j] = False

longest_path(0, 1, 0)

print(longest_found)
            

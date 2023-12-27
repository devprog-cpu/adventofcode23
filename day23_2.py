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

start = (0, 1)
finish = (m-1, n-2)

directions = {(0, 1), (0, -1), (1, 0), (-1, 0)}
junctions = set()

for i in range(m):
    for j in range(n):
        if lines[i][j] == '#': continue
        c = 0
        for di, dj in directions:
            ni = i + di
            nj = j + dj
            if ni < 0 or ni >= m or nj < 0 or nj >= n:
                continue
            if lines[ni][nj] != '#': c += 1
        if c > 2:
            junctions.add((i, j))

junctions.add(start)
junctions.add(finish)
graph = collections.defaultdict(list)

def find_junction(ci, cj, pi, pj):
    if (ci, cj) in junctions:
        return (ci, cj, 0)
    for di, dj in directions:
        ni = ci + di
        nj = cj + dj
        if ni < 0 or ni >= m or nj < 0 or nj >= n:
            continue
        if ni == pi and nj == pj: continue
        if lines[ni][nj] == '#': continue
        res = find_junction(ni, nj, ci, cj)
        return (res[0], res[1], res[2] + 1)

def find_neighbour_junctions(si, sj, graph):
    # print('calling find_neighbour_junctions', si, sj)
    for di, dj in directions:
        ni = si + di
        nj = sj + dj
        if ni < 0 or ni >= m or nj < 0 or nj >= n:
            continue
        if lines[ni][nj] == '#': continue
        # print('calling find_junction', ni, nj, si, sj)
        res = find_junction(ni, nj, si, sj)
        graph[(si, sj)].append((res[0], res[1], res[2] + 1))
        
print(len(junctions), 'junctions', junctions)

for ci, cj in junctions:
    find_neighbour_junctions(ci, cj, graph)

visited = set()

longest_found = 0

def longest_path(i, j, steps):
    # print('Called', i, j, steps)
    if i == m - 1:
        global longest_found
        if steps > longest_found:
            print(steps)
        longest_found = max(longest_found, steps)
        return
    visited.add((i, j))
    for ni, nj, ns in graph[(i, j)]:
        if (ni, nj) not in visited:
            longest_path(ni, nj, steps + ns)
    visited.remove((i, j))

longest_path(*start, 0)

print('Longest path found', longest_found)


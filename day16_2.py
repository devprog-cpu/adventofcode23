import itertools
import functools
import math
import collections
import sys
import operator

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def next_cells(curr, prev, char):
    cx, cy = curr
    px, py = prev
    if (char, px, py) == ('.', cx - 1, cy): return [(cx + 1, cy)]
    if (char, px, py) == ('.', cx + 1, cy): return [(cx - 1, cy)]
    if (char, px, py) == ('.', cx, cy - 1): return [(cx, cy + 1)]
    if (char, px, py) == ('.', cx, cy + 1): return [(cx, cy - 1)]

    if (char, px, py) == ('/', cx - 1, cy): return [(cx, cy - 1)]
    if (char, px, py) == ('/', cx + 1, cy): return [(cx, cy + 1)]
    if (char, px, py) == ('/', cx, cy - 1): return [(cx - 1, cy)]
    if (char, px, py) == ('/', cx, cy + 1): return [(cx + 1, cy)]

    if (char, px, py) == ('\\', cx - 1, cy): return [(cx, cy + 1)]
    if (char, px, py) == ('\\', cx + 1, cy): return [(cx, cy - 1)]
    if (char, px, py) == ('\\', cx, cy - 1): return [(cx + 1, cy)]
    if (char, px, py) == ('\\', cx, cy + 1): return [(cx - 1, cy)]

    if (char, px, py) == ('|', cx - 1, cy): return [(cx + 1, cy)]
    if (char, px, py) == ('|', cx + 1, cy): return [(cx - 1, cy)]
    if (char, px, py) == ('|', cx, cy - 1): return [(cx + 1, cy), (cx - 1, cy)]
    if (char, px, py) == ('|', cx, cy + 1): return [(cx + 1, cy), (cx - 1, cy)]

    if (char, px, py) == ('-', cx - 1, cy): return [(cx, cy - 1), (cx, cy + 1)]
    if (char, px, py) == ('-', cx + 1, cy): return [(cx, cy - 1), (cx, cy + 1)]
    if (char, px, py) == ('-', cx, cy - 1): return [(cx, cy + 1)]
    if (char, px, py) == ('-', cx, cy + 1): return [(cx, cy - 1)]

    raise ValueError(f'Did not expect {(grid[cx][cy], px, py)}')

m = len(lines)
n = len(lines[0])

grid = lines

def dfs(curr, prev):
    stack = [(curr, prev)]
    visited = collections.defaultdict(set)

    while stack:
        curr, prev = stack.pop()

        if prev in visited[curr]: continue
        visited[curr].add(prev)

        for nx, ny in next_cells(curr, prev, grid[curr[0]][curr[1]]):
            if 0 <= nx < m and 0 <= ny < n:
                stack.append(((nx, ny), curr))

    return len(visited)

ans = 0
for j in range(n):
    ans = max(ans, dfs((0, j), (-1, j)))
    ans = max(ans, dfs((m-1, j), (m, j)))
for i in range(m):
    ans = max(ans, dfs((i, 0), (i, -1)))
    ans = max(ans, dfs((i, n-1), (i, n)))

print(ans)



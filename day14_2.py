import itertools
import functools
import math
import collections
import sys
import operator

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

total_lines = len(lines)
line_len = len(lines[0])
cycles_to_run = 1000000000

grid = [list(line) for line in lines]
seen = dict()

def tilt_north():
    for i in range(line_len):
        free = 0
        for j in range(total_lines):
            if grid[j][i] == 'O':
                if free != j:
                    grid[j][i] = '.'
                    grid[free][i] = 'O'
                free += 1
            elif grid[j][i] == '#':
                free = j + 1

def tilt_south():
    for i in range(line_len):
        free = total_lines - 1
        for j in range(total_lines-1, -1, -1):
            if grid[j][i] == 'O':
                if free != j:
                    grid[j][i] = '.'
                    grid[free][i] = 'O'
                free -= 1
            elif grid[j][i] == '#':
                free = j - 1

def tilt_west():
    for i in range(total_lines):
        free = 0
        for j in range(line_len):
            if grid[i][j] == 'O':
                if free != j:
                    grid[i][j] = '.'
                    grid[i][free] = 'O'
                free += 1
            elif grid[i][j] == '#':
                free = j + 1

def tilt_east():
    for i in range(total_lines):
        free = line_len - 1
        for j in range(line_len - 1, -1, -1):
            if grid[i][j] == 'O':
                if free != j:
                    grid[i][j] = '.'
                    grid[i][free] = 'O'
                free -= 1
            elif grid[i][j] == '#':
                free = j - 1

c = 0
st = ''
while c < cycles_to_run:
    tilt_north()
    tilt_west()
    tilt_south()
    tilt_east()
    c += 1

    st = ''.join([''.join(line) for line in grid])
    if (r := seen.get(st)) is not None:
        print(f'Cycle {c} is same as {r}')
        break
    else:
        seen[st] = c

    if c % 10000 == 0: print('At cycle', c)

    # print('After cycle', c)
    # for line in grid:
    #     print(''.join(line))
    # print()

ans = 0
print('Done after cycles', c)

r = seen[st]
final_cycle = r + ((cycles_to_run - c) % (c-r))
print('Final cycle is', final_cycle)
final_state = [k for k, v in seen.items() if v == final_cycle][0]
print(final_state)


weight = total_lines
for i, c in enumerate(final_state):
    if i != 0 and i % line_len == 0: weight -= 1
    if c == 'O':
        ans += weight

print(ans)

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

dirs = ['R', 'D', 'L', 'U']

instructions = []
for line in lines:
    sp = line.split(' ')[2]
    instructions.append((dirs[int(sp[-2])], int(sp[2:-2], 16)))

# Perhaps could be solved similar to day10 part 2 ??


'''
sU, sD, sL, sR = 0, 0, 0, 0
lr, ud = 0, 0
for direction, moves in instructions:
    match direction:
        case 'L': lr -= moves
        case 'R': lr += moves
        case 'U': ud -= moves
        case 'D': ud += moves
    sR = max(sR, lr)
    sL = min(sL, lr)
    sU = min(sU, ud)
    sD = max(sD, ud)

print(sU, sD, sL, sR, file = sys.stderr)
print(sD - sU, sR - sL, file = sys.stderr)
exit()

y_offset = -sL
x_offset = -sU

disp = [[' '] * (sR + y_offset + 1) for _ in range(sD + x_offset + 1)]

cx, cy = 0, 0
disp[cx + x_offset][cy + y_offset] = 'S'
for direction, moves in instructions:
    match direction:
        case 'L':
            for i in range(cy, cy - moves - 1, -1):
                disp[cx + x_offset][i + y_offset] = '#'
            cy -= moves
        case 'R':
            for i in range(cy, cy + moves + 1):
                disp[cx + x_offset][i + y_offset] = '#'
            cy += moves
        case 'U':
            for i in range(cx, cx - moves - 1, -1):
                disp[i + x_offset][cy + y_offset] = '#'
            cx -= moves
        case 'D':
            for i in range(cx, cx + moves + 1):
                disp[i + x_offset][cy + y_offset] = '#'
            cx += moves
for i in range(sU, sD + 1):
    print(''.join(disp[i + x_offset]))
'''


# tracemalloc.start()

grid = collections.defaultdict(list)
cx, cy = 0, 0
mincx, maxcx = float('inf'), float('-inf')
mincy, maxcy = float('inf'), float('-inf')
connected_to = 'D' if instructions[-1][0] == 'U' else 'U'
updowns = []
for direction, moves in instructions:
    match direction:
        case 'L':
            # grid[cx].append((cy - moves, cy))
            grid[cx].append([cy - moves, connected_to, 'MM', moves])
            cy -= moves
        case 'R':
            # grid[cx].append((cy, cy + moves))
            grid[cx].append([cy, connected_to, 'MM', moves])
            cy += moves
        case 'U':
            grid[cx][-1][2] = 'U'
            # for i in range(cx - 1, cx-moves, -1):
            #     # grid[i].append((cy, cy))
            #     grid[i].append([cy])
            updowns.append((cx - moves + 1, cx, cy))
            cx -= moves
        case 'D':
            grid[cx][-1][2] = 'D'
            # for i in range(cx + 1, cx+moves):
            #     # grid[i].append((cy, cy))
            #     grid[i].append([cy])
            updowns.append((cx + 1, cx + moves, cy))
            cx += moves
    connected_to = 'D' if direction == 'U' else 'U'
    mincx = min(mincx, cx)
    maxcx = max(maxcx, cx)
    mincy = min(mincy, cy)
    maxcy = max(maxcy, cy)


# print('x = ', mincx, maxcx)
# print('y = ', mincy, maxcy)
# print('grid len', len(grid))

ends = []
ans = 0
area = True
for j in range(mincx, maxcx + 1):
    ends = [[cy] for s, e, cy in updowns if j >= s and j < e]
    arr = grid[j]
    arr.extend(ends)
    arr.sort()
    n = len(arr)

    # print(arr)
    c = 0

    inside = 0
    for i in range(n):
        if len(arr[i]) == 4:
            c += arr[i][3] + 1
            if arr[i][1] != arr[i][2]: inside = 1 - inside
            if inside and area:
                c += arr[i+1][0] - (arr[i][0] + arr[i][3] + 1)
        else:
            inside = 1 - inside
            c += 1
            if inside and area:
                c += arr[i+1][0] - arr[i][0] - 1
    # print('c', c)
    ans += c
    ends = []
    arr = []
    del grid[j]

# print(grid)
print(ans)

'''
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)
'''


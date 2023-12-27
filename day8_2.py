import itertools
import operator
import collections
import functools
import math

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

steps = 'LLRLRRRLLLRLRRLRRRLRLRRLRLRLRRRLRRRLRLRLRRLLRRRLRRLRRLLRLRRRLRLRLLRRRLLRRRLRLRRRLRRRLRRRLLLRRRLRRLRRLRLRRLRLRRRLRLRRLRLRLRRRLRLLLRRRLLLRLRRRLRLRRLRLRLRLRRLRRLRRLRLRRRLRRRLRRLRRRLRRLRRLRRRLLRLRRLLLRRLRRLRLRLLLRRLRRLRRRLRRLLRLRRRLRRRLRRLRRLRLRRLRLRRRLRRLRRRLLRRRLRLRLLLRRRLLLRRLLRRLRLRRLRLLLRRRR'
# steps = 'LR'
steps_len = len(steps)
d = {'L': 0, 'R': 1}

graph = dict()
stops = dict()
vals = dict()

for line in lines:
    sp = line.split(' = ')
    st = sp[1].split(',')
    tup = (st[0][1:], st[1][1:-1])
    graph[sp[0]] = tup
    if sp[0][-1] == 'A':
        stops[sp[0]] = dict()
        vals[sp[0]] = None

starts = list(stops.keys())


def update_stops(start):
    i = 0
    require = 0
    curr = start
    while True:
        curr = graph[curr][d[steps[i]]]
        require += 1
        if curr[-1] == 'Z':
            if stops[start].get((curr, i)) is None:
                stops[start][(curr, i)] = require
                vals[start] = require
            else:
                break
        i = (i + 1) % steps_len

for curr in starts:
    update_stops(curr)

print(stops)
print(vals)

print(math.lcm(*vals.values()))

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


weights = [total_lines] * line_len

ans = 0

row = total_lines
for line in lines:
    for j in range(line_len):
        if line[j] == 'O':
            ans += weights[j]
            weights[j] -= 1
        elif line[j] == '#':
            weights[j] = row - 1
    row -= 1

print(ans)


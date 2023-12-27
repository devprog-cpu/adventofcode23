import itertools
import functools
import math
import collections
import sys
import operator

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

for i in range(len(lines)):
    sp = lines[i].split(' ')
    lines[i] = [list(sp[0]), [int(a) for a in sp[1].split(',')]]

def get_ways(spring, nums):

    n = len(spring)
    ans = 0
    def gen(i):
        nonlocal ans
        if i == n:
            li = list(map(len, filter(operator.truth, ''.join(spring).split('.'))))
            if li == nums: ans += 1
            return
        if spring[i] == '?':
            spring[i] = '.'
            gen(i+1)
            spring[i] = '#'
            gen(i+1)
            spring[i] = '?'
        else:
            gen(i+1)
    gen(0)
    return ans

ans = 0
for line in lines:
    res = get_ways(*line)
    # print(res)
    ans += res

print(ans)


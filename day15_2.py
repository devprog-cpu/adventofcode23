import itertools
import functools
import math
import collections
import sys
import operator

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

line = lines[0]
seq = line.split(',')

def get_hash(s):
    ans = 0
    for c in s:
        ans += ord(c)
        ans *= 17
        ans %= 256
    return ans

hashes = [dict() for i in range(256)]
lists = [collections.deque() for i in range(256)]

for s in seq:
    if '=' in s:
        sp = s.split('=')
        f = int(sp[1])
        h = get_hash(sp[0])
        if sp[0] not in hashes[h]:
            lists[h].append(sp[0])
        hashes[h][sp[0]] = f
    else:
        sp = s[:-1]
        h = get_hash(sp)
        if sp in hashes[h]:
            del hashes[h][sp]

# print(hashes)
# print(lists)

ans = 0
for box in range(256):
    idx = len(hashes[box])
    if idx == 0: continue
    lists[box].reverse()
    for s in lists[box]:
        if (v := hashes[box].get(s)) is not None:
            ans += (box + 1) * idx * v
            # print(f'Adding {v} at {idx} for {s} in box {box+1}', 'ans', ans)
            idx -= 1
            hashes[box].pop(s)

print(ans)

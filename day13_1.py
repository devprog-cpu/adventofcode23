import itertools
import functools
import math
import collections
import sys
import operator

with open(sys.argv[1], 'r') as f:
    lines = [line.strip() for line in f.readlines()]

def check_palindrome(pattern):
    n = len(pattern)

    for i in range(1, n):
        found = True
        l, r = i-1, i
        while r < n and l >= 0:
            if pattern[r] != pattern[l]:
                found = False
            r += 1
            l -= 1
        if found: return i
    return None


def get_summary(pattern):

    if (res := check_palindrome(pattern)) is not None:
        return res * 100

    rows = len(pattern)
    cols = len(pattern[0])
    pats = [''.join(pattern[j][i] for j in range(rows)) for i in range(cols)]
    
    if (res := check_palindrome(pats)) is not None:
        return res

    for l in pattern:
        print(l)
    print(pats)
    raise ValueError('No mirror found')


ans = 0
pattern = []
i = 0
while i < len(lines):
    while i < len(lines) and lines[i] != '':
        pattern.append(lines[i])
        i += 1
    print('checking pattern ending on', i)
    ans += get_summary(pattern)
    pattern = []
    i += 1


print(ans)

import itertools
import operator
import collections
import functools
import math

def next_value(arr):
    if len(set(arr)) == 1:
        return arr[0]
    diff_arr = [arr[i] - arr[i-1] for i in range(1, len(arr))]
    return arr[0] - next_value(diff_arr)

with open('test.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

ans = 0
for line in lines:
    arr = [int(x) for x in line.split()]
    val = next_value(arr)
    ans += val

print(ans)


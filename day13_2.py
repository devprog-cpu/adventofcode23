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
    lines[i] = [sp[0], [int(a) for a in sp[1].split(',')]]

def get_ways_try1(spring_1, nums_1):
    springs = '?'.join([spring_1] * 5)
    nums = nums_1 * 5

    sn = len(springs)
    nn = len(nums)
    # print(sn, nn)

    springs += '..'
    nums.append(0)
    # print('Processing spring', springs)
    # print('nums', nums)

    dp = [[0] * (sn + 2) for _ in range(nn + 1)]
    dp[nn][sn] = 1
    dp[nn][sn + 1] = 1
    for i in range(sn-1, -1, -1):
        if springs[i] == '#': break
        dp[nn][i] = 1

    # print(f'dp[{nn}]', dp[nn])


    for ni in range(nn-1, -1, -1):
        for si in range(sn-1, -1, -1):
            if springs[si] == '.' or springs[si] == '?':
                dp[ni][si] = dp[ni][si+1]
            if springs[si] == '#' or springs[si] == '?':
                if si+nums[ni] <= sn and \
                    springs[si:si+nums[ni]].count('.') == 0 and \
                    springs[si+nums[ni]] in ('.', '?'):
                    dp[ni][si] += dp[ni+1][si+nums[ni]+1]
        # print(f'dp[{ni}]', dp[ni])

    return dp[0][0]

def get_ways(spring_1, nums_1):
    springs = '?'.join([spring_1] * 5)
    nums = nums_1 * 5

    sn = len(springs)
    nn = len(nums)
    # print(sn, nn)

    springs += '..'
    nums.append(0)
    # print('Processing spring', springs)
    # print('nums', nums)

    prev = [0] * (sn + 2)
    curr = [0] * (sn + 2)
    prev[sn] = 1
    prev[sn + 1] = 1
    for i in range(sn-1, -1, -1):
        if springs[i] == '#': break
        prev[i] = 1

    # print('prev', prev)


    for ni in range(nn-1, -1, -1):
        for si in range(sn-1, -1, -1):
            if springs[si] == '.' or springs[si] == '?':
                curr[si] = curr[si+1]
            if springs[si] == '#' or springs[si] == '?':
                if si+nums[ni] <= sn and \
                    springs[si:si+nums[ni]].count('.') == 0 and \
                    springs[si+nums[ni]] in ('.', '?'):
                    curr[si] += prev[si+nums[ni]+1]
        # print('curr', curr)
        prev = curr
        curr = [0] * (sn + 2)

    return prev[0]

ans = 0
for line in lines:
    res = get_ways(*line)
    print(res)
    ans += res

print(ans)


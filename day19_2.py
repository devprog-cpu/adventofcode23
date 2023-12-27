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

workflows = dict()

while lines[0] != '':
    line = lines[0]
    lines = lines[1:]

    i1 = line.index('{')
    wf_name = line[:i1]
    l1 = line[i1+1:-1].split(',')
    rules = []
    for rule in l1[:-1]:
        sp = rule.split(':')
        cnd, dest = sp[0], sp[1]
        if '<' in cnd:
            sp = cnd.split('<')
            rules.append((sp[0], '<', int(sp[1]), dest))
        else:
            sp = cnd.split('>')
            rules.append((sp[0], '>', int(sp[1]), dest))
    rules.append((l1[-1],))
    workflows[wf_name] = rules


def process_workflow(part, wf):
    if wf == 'A':
        global ans
        ans += math.prod(max(0, s[1] - s[0] + 1) for s in part.values())
        # print('Accepted', part, 'ans', ans)
        return
    if wf == 'R': return
    
    cop = part.copy()

    # print('Processing workflow', wf, '---', part)
    # input('')
    for rule in workflows[wf][:-1]:
        # print('Checking', rule)
        if rule[1] == '<':
            before = part[rule[0]]
            part[rule[0]] = (part[rule[0]][0], rule[2] - 1)
            process_workflow(part, rule[3])
            part[rule[0]] = before
            part[rule[0]] = (rule[2], part[rule[0]][1])
        elif rule[1] == '>':
            before = part[rule[0]]
            part[rule[0]] = (rule[2] + 1, part[rule[0]][1])
            process_workflow(part, rule[3])
            part[rule[0]] = before
            part[rule[0]] = (part[rule[0]][0], rule[2])
    process_workflow(part, workflows[wf][-1][0])
    for k in cop.keys():
        part[k] = cop[k]

'''
def is_accepted(part):
    curr = 'in'
    # print('Processing', part, 'for', curr)
    while True:
        curr = process_workflow(part, curr)
        # print('new workflow', curr)
        if curr == 'A': return True
        if curr == 'R': return False
'''

ans = 0
min_val, max_val = 1, 4000
part = {'x': (min_val, max_val), 'm': (min_val, max_val), 'a': (min_val, max_val), 's': (min_val, max_val), }
process_workflow(part, 'in')

print(ans)


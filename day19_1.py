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
    for rule in workflows[wf][:-1]:
        # print('Checking', rule)
        if rule[1] == '<' and part[rule[0]] < rule[2]: return rule[3]
        if rule[1] == '>' and part[rule[0]] > rule[2]: return rule[3]
    return workflows[wf][-1][0]

def is_accepted(part):
    curr = 'in'
    # print('Processing', part, 'for', curr)
    while True:
        curr = process_workflow(part, curr)
        # print('new workflow', curr)
        if curr == 'A': return True
        if curr == 'R': return False

ans = 0
lines = lines[1:]
while lines:
    part_line = lines[0]
    lines = lines[1:]

    part = dict()
    attrs = part_line[1:-1].split(',')
    for attr in attrs:
        sp = attr.split('=')
        part[sp[0]] = int(sp[1])
    
    if is_accepted(part):
        ans += sum(part.values())

print(ans)


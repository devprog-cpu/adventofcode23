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

# test answer = 54 = 9 * 6

graph = collections.defaultdict(list)
edges = set()

for line in lines:
    sp = line.split(': ')
    u = sp[0]
    vs = sp[1].split(' ')
    graph[u].extend(vs)
    for v in vs:
        graph[v].append(u)
        edges.add((u, v))
        
n = len(graph)
print('Number of nodes', n)
no_of_edges = sum(len(v) for v in graph.values()) // 2
print('Number of edges', no_of_edges)

def shortest_distance(src):
    global graph
    dist = collections.defaultdict(lambda: math.inf)
    q = collections.deque([src])
    dist[src] = 0

    while q:
        u = q.popleft()
        du = dist[u]
        for v in graph[u]:
            if dist[v] == math.inf:
                dist[v] = du + 1
                q.append(v)
    return dist

temp = list(graph.keys())[0]
dist_temp = shortest_distance(temp)
dist_temp_max = max(dist_temp.values())

node1 = [k for k, v in dist_temp.items() if v == dist_temp_max][0]
dist_node1 = shortest_distance(node1)
dist_node1_max = max(dist_node1.values())

node2 = [k for k, v in dist_node1.items() if v == dist_node1_max][0]
dist_node2 = shortest_distance(node2)

print('Node1', node1, 'Node2', node2)

remaining = set(graph.keys())
s1 = {node1}
s2 = {node2}
remaining.discard(node1)
remaining.discard(node2)

while remaining and len(edges) > 3:
    t1, t2 = set(), set()
    for u in s1:
        for v in graph[u]:
            if v in remaining:
                t1.add(v)
                remaining.discard(v)
                edges.discard((u, v))
                edges.discard((v, u))
    for u in s2:
        for v in graph[u]:
            if v in remaining:
                t2.add(v)
                remaining.discard(v)
                edges.discard((u, v))
                edges.discard((v, u))

    s1.update(t1)
    s2.update(t2)
    
print('Remaining nodes', remaining)
print('Remaining edges', edges)
print('Sizes', len(s1), len(s2))
print('Answer', len(s1) * len(s2))

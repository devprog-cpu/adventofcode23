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

BROADCASTER = 'broadcaster'
FLIPFLOP = '%'
CONJUNCTION = '&'
LOW = True
HIGH = False

modules = dict()
state = dict()
types = dict()
pulse_counts = []

for line in lines:
    src, l1 = line.split(' -> ')
    dests = l1.split(', ')
    if src == BROADCASTER:
        modules[BROADCASTER] = dests
        types[BROADCASTER] = BROADCASTER
    elif src[0] == FLIPFLOP:
        modules[src[1:]] = dests
        state[src[1:]] = HIGH
        types[src[1:]] = FLIPFLOP
    elif src[0] == CONJUNCTION:
        modules[src[1:]] = dests
        state[src[1:]] = dict()
        types[src[1:]] = CONJUNCTION
    else:
        raise ValueError('Module of unknown type', line)

for name, dests in modules.items():
    for d in dests:
        if types.get(d) == CONJUNCTION:
            state[d][name] = LOW

def is_reset():
    for name, value in state.items():
        if types[name] == FLIPFLOP and value != HIGH:
            return False
        elif types[name] == CONJUNCTION and any(x == HIGH for x in value.values()):
            return False
    return True

def process_pulse():
    counter = [1, 0] # low, high
    process_q = []
    pending = collections.defaultdict(list)

    for dest in modules[BROADCASTER]:
        counter[0] += 1
        process_q.append(dest)
        pending[dest].append((BROADCASTER, LOW))

    while process_q:
        curr, process_q = process_q[0], process_q[1:]

        pulse, pending[curr] = pending[curr][0], pending[curr][1:]
        src, sig = pulse
        if types.get(curr) == FLIPFLOP:
            if sig == HIGH: continue
            signal_to_send = state[curr]
            state[curr] = LOW if state[curr] == HIGH else HIGH
        elif types.get(curr) == CONJUNCTION:
            state[curr][src] = sig
            signal_to_send = LOW if all(x == HIGH for x in state[curr].values()) else HIGH
        else:
            continue
            # raise ValueError('Module of unknown type', curr)
                
        idx = 0 if signal_to_send == LOW else 1
        for dest in modules[curr]:
            pending[dest].append((curr, signal_to_send))
            process_q.append(dest)
            counter[idx] += 1

    pulse_counts.append(tuple(counter))

total_cycles = 1000
cycle = 0
while cycle < total_cycles:
    process_pulse()
    cycle += 1
    if is_reset(): break

repeating_after = len(pulse_counts)
print('repeating_after', repeating_after)
print('pulse_counts', pulse_counts)

low_count, high_count = 0, 0
for i in range(total_cycles):
    low_count += pulse_counts[i % repeating_after][0]
    high_count += pulse_counts[i % repeating_after][1]

print(low_count * high_count)


import bisect 
import itertools

def to_array(map_lines):
    arr = []
    for line in map_lines:
        sp = line.split()
        arr.append((int(sp[1]), int(sp[2]), int(sp[0])))
    arr.sort()
    return arr

def map_range(start, length, mapping):
    # print('Called map_range', start, length)
    if length <= 0: return []
    result = []
    idx = bisect.bisect_right(mapping, start, key = lambda x: x[0]) - 1
    if idx == -1 or start > mapping[idx][0] + mapping[idx][1] - 1:
        if idx + 1 < len(mapping):
            take_len = min(length, mapping[idx+1][0] - start)
            result.append((start, take_len))
            result.extend(map_range(mapping[idx+1][0], length - take_len, mapping))
        else:
            result.append((start, length))
    else:
        mapped = mapping[idx][2] + start - mapping[idx][0]
        take_len = min(length, mapping[idx][2] + mapping[idx][1] - mapped)
        result.append((mapped, take_len))
        result.extend(map_range(start + take_len, length - take_len, mapping))
    return result
        

def get_seeds_ranges_and_mapping(lines):
    seeds_arr = [int(x) for x in lines[0][6:].split()]
    seeds = []
    maps = []
    for i in range(0, len(seeds_arr), 2):
        seeds.append((seeds_arr[i], seeds_arr[i+1]))

    lines = lines[3:]
    while lines:
        new_start = 0
        while new_start < len(lines) and lines[new_start] != '':
            new_start += 1
        maps.append(to_array(lines[:new_start]))
        lines = lines[new_start+2:]

    return (seeds, maps)

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

seeds, maps = get_seeds_ranges_and_mapping(lines)
original_seeds = seeds
for mapping in maps:
    ranges = []
    for start, length in seeds:
        print('Processing range', start, length)
        ranges.extend(map_range(start, length, mapping))
    print(ranges)
    seeds = ranges

ans = float('inf')
for s, _ in seeds:
    ans = min(ans, s)

print(ans)

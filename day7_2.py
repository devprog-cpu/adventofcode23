import itertools
import operator
import collections
import functools

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

with open('input.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

def get_hand_type(hand):
    ctr = collections.Counter(hand)
    jokers = ctr['J']
    if jokers != 5:
        del ctr['J']
        top = ctr.most_common(1)[0][0]
        ctr[top] += jokers 
    values = list(sorted(ctr.values(), reverse = True))
    if values[0] == 5: return 7
    if values[0] == 4: return 6
    if values[0] == 3 and values[1] == 2: return 5
    if values[0] == 3: return 4
    if values[0] == 2 and values[1] == 2: return 3
    if values[0] == 2: return 2
    return 1


def hand_cmp(hand1, hand2):
    for i in range(5):
        o1 = order.index(hand1[i])
        o2 = order.index(hand2[i])
        if o1 != o2: return o2 - o1
    return 0

def full_cmp(hand1, hand2):
    t1 = get_hand_type(hand1[0])
    t2 = get_hand_type(hand2[0])
    set_hands.add((hand1[0], t1))
    set_hands.add((hand2[0], t2))
    if t1 != t2:
        return t1 - t2
    return hand_cmp(hand1[0], hand2[0])


set_hands = set()
hands = []
for line in lines:
    sp = line.split()
    hands.append((sp[0], int(sp[1])))

hands.sort(key = functools.cmp_to_key(full_cmp))
print(set_hands)
print(hands)

ans = 0
for i in range(1, len(hands)+1):
    ans += i * hands[i-1][1]

print(ans)

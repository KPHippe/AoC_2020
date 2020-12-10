from copy import deepcopy
from collections import Counter

example_input = '''\
16
10
15
5
1
11
7
19
6
12
4'''

def parse_input(raw_data):
    return [int(e) for e in raw_data.split('\n')]

def find_1_and_3_differences(joltage_adapters):
    one_list, three_list = 0, 0
    if joltage_adapters[0] == 1:
        one_list+= 1
    elif joltage_adapters[0] == 3:
        three_list += 1

    for i in range(len(joltage_adapters)-1):
        cur_adapter = joltage_adapters[i]
        next_adapter = joltage_adapters[i+1]

        if next_adapter - cur_adapter == 1:
            one_list += 1
        elif next_adapter -cur_adapter == 3:
            three_list += 1

    three_list +=1
    return one_list, three_list

def find_all_combinations(joltage_adapters):
    adapters = deepcopy(joltage_adapters)
    adapters.append(adapters[-1] + 3)

    cache = Counter()
    cache[0] = 1

    for adapter in adapters:
        cache[adapter] = cache[adapter - 1] + cache[adapter - 2] + cache[adapter - 3]

    return cache[adapters[-1]]


if __name__ == '__main__':
    # joltage_adapters = sorted(parse_input(example_input))
    joltage_adapters = sorted(parse_input(open('day_10_input.txt').read().strip()))

    one, three = find_1_and_3_differences(joltage_adapters)

    print(f"One: {one}, Three: {three}, answer: {str(one*three)}")

    total_combinations = find(joltage_adapters)
    print(f"Total combinations: {total_combinations}")

example_input = '''\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

def parse_input(raw_input):
    return [int(e) for e in raw_input.split('\n')]

def find_weakness(data, preamble_length):

    for i in range(preamble_length, len(data)):
        possible_contributors = data[i-preamble_length:i]
        target = data[i]
        valid = False
        for lhs in possible_contributors:
            if (target - lhs) in possible_contributors:
                valid = True
        if not valid:
            return i, target

def find_contiguous_set(data, bad_index, bad_target):
    for i in range(len(data)):
        if i == bad_index:
            continue
        cur_set = [data[i]]
        range_index = i +1
        while sum(cur_set) < bad_target:
            cur_set.append(data[range_index])
            range_index += 1
            if sum(cur_set) == bad_target:
                return cur_set

    return None

if __name__ == '__main__':
    # data = parse_input(example_input)
    data = parse_input(open('day_9_input.txt').read().strip())

    weakness = find_weakness(data, 25)
    print(f'The weakness is index {weakness[0]} with value: {weakness[1]}')

    weakness_set = sorted(find_contiguous_set(data, weakness[0], weakness[1]))
    print(f'Stage_2 answer: {weakness_set[0] + weakness_set[-1]}')

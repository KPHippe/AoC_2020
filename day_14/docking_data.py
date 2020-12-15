example_input = '''\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

from copy import deepcopy

def apply_mask(mask, value):  # mask = binary string, value = dec value
    value_binary = f"{value:36b}".replace(' ', '0')
    new_value = ''
    for i in range(len(mask)):
        new_value += value_binary[i] if mask[i] == 'X' else mask[i]
    return int(new_value, 2)

def mask_location(mask, addr):
    addr_binary = f"{addr:36b}".replace(' ', '0')
    new_addr = []
    for i in range(len(mask)):
        if mask[i] == '0':
            new_addr.append( addr_binary[i])

        elif mask[i] == 'X':
            new_addr.append(mask[i])

        else: # 1
            new_addr.append(mask[i])

    x_occurences = [i for i in range(len(new_addr)) if new_addr[i] == 'X']
    for i in range(2**len(x_occurences)):
        i_binary = list(f"{i:b}")
        zeroes_to_add = ['0'] * (len(x_occurences) - len(i_binary))
        i_binary = zeroes_to_add + i_binary
        for ind, sub_val in enumerate(i_binary):
            target_idx = x_occurences[ind]
            new_addr[target_idx] = sub_val
        yield int(''.join(new_addr), 2)

def apply_initialization(program):
    mem = {}
    current_mask = ''
    for line in program:
        key_word, token = line.split(' = ')
        if key_word == 'mask':
            current_mask = token
        else:
            token = int(token)
            location = int(key_word.strip('mem[]'))
            mem[location] = apply_mask(current_mask, token)
    return sum(mem.values())

def mask_addresses(program):
    mem = {}
    current_mask = ''
    for line in program:
        key_word, token = line.split(' = ')
        if key_word == 'mask':
            current_mask = token
        else:
            token = int(token)
            location = int(key_word.strip('mem[]'))
            for mut_location in mask_location(current_mask, location):
                mem[mut_location] = token

    return sum(mem.values())


if __name__ == '__main__':
    # program = example_input.splitlines()
    program = open('day_14_input.txt', 'r').read().splitlines()
    sum_vals = apply_initialization(program)
    print(f'Part 1 answer: {sum_vals}')

    sum_vals_2 = mask_addresses(program)
    print(f'Part 2 answer: {sum_vals_2}')

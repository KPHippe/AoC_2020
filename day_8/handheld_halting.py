from copy import deepcopy

example_input = '''\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

accumulator = 0

def parse_instructions(raw_instructions):
    instructions = []
    for line in raw_instructions.split('\n'):
        instruction, val = line.split()
        instructions.append([instruction, int(val), 0])
    return instructions

def execute_instruction(instruction, val):
    #returns step
    global accumulator
    if 'nop' in instruction:
        return 1
    if 'acc' in instruction:
        accumulator += val
        return 1
    if 'jmp' in instruction:
        return val

def run_program(instructions):
    global accumulator
    accumulator = 0
    cur_instruction = 0
    while cur_instruction < len(instructions) and instructions[cur_instruction][2] < 50:
        instruction, val, visited = instructions[cur_instruction]
        instructions[cur_instruction][2] += 1
        # print(cur_instruction, instruction, val, visited)
        step = execute_instruction(instruction, val)
        cur_instruction += step

    if cur_instruction >= len(instructions):

        return True
    else:
        return False
    # print(cur_instruction, instruction, val, visited)
    # print(f"Current accumulator: {accumulator}")

def find_bugged_code(base_instructions):
    for i, instruction in enumerate(base_instructions):
        if 'nop' in instruction[0]:
            new_instruction = ['jmp', instruction[1], 0]
            permutation_instructions = deepcopy(base_instructions)
            permutation_instructions[i]= new_instruction

            if run_program(permutation_instructions):
                return i, new_instruction
        if 'jmp' in instruction[0]:
            new_instruction = ['nop', instruction[1], 0]
            permutation_instructions = deepcopy(base_instructions)
            permutation_instructions[i]= new_instruction

            if run_program(permutation_instructions):
                return i, new_instruction
        print(f"{i} of {len(base_instructions)}")



if __name__ == '__main__':
    # instructions = parse_instructions(example_input)
    instructions = parse_instructions(open('day_8_input.txt', 'r').read().strip())
    # print(instructions)
    # run_program(instructions)

    i, new_instruction = find_bugged_code(instructions)

    final_instruction_set = deepcopy(instructions)
    final_instruction_set[i] = new_instruction
    if run_program(final_instruction_set):
        print(f'Succesful run, accumulator: {accumulator}, instruction: {new_instruction}, position: {i}')

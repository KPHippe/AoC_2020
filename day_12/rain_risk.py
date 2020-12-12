example_input = '''\
F10
N3
F7
R90
F11'''


def parse_input(raw_input):
    instructions = []
    for raw_instruction in raw_input.split('\n'):
        command, value = str(raw_instruction[:1]), int(raw_instruction[1:])
        instructions.append((command, value))

    return instructions

def navigate_1(instructions):
    dir = 90
    x, y = 0, 0

    for (command, value) in instructions:
        if 'N' in command:
            y += value
        if 'S' in command:
            y -= value
        if 'E' in command:
            x += value
        if 'W' in command:
            x -= value
        if 'R' in command:
            pre_dir = dir
            dir = (dir + value)% 360
        if 'L' in command:
            pre_dir = dir
            dir = (dir - value) % 360
        if 'F' in command:
            if dir == 0: #north
                y += value
            if dir == 90:  #east
                x += value
            if dir == 180: #south
                y -= value
            if dir == 270: #west
                x -= value

    return x, y

def navigate_2(instructions):
    x, y = 0, 0

    waypoint_modifiers = [10, 1]

    for (command, value) in instructions:
        if 'N' in command:
            waypoint_modifiers[1] += value
        if 'S' in command:
            waypoint_modifiers[1] -= value
        if 'E' in command:
            waypoint_modifiers[0] += value
        if 'W' in command:
            waypoint_modifiers[0] -= value
        if 'R' in command:
            for i in range(value//90):
                waypoint_modifiers = [waypoint_modifiers[1], -waypoint_modifiers[0]]
        if 'L' in command:
            for i in range(value//90):
                waypoint_modifiers = [-waypoint_modifiers[1], waypoint_modifiers[0]]
        if 'F' in command:
            x += (value * waypoint_modifiers[0])
            y += (value * waypoint_modifiers[1])

    return x, y


if __name__ == '__main__':
    # instructions = parse_input(example_input)
    instructions = parse_input(open('day_12_input.txt').read().strip())

    x, y = navigate_1(instructions)
    print(f"Coordinates: {x}, {y} answer: {abs(x) + abs(y)}")

    x, y = navigate_2(instructions)
    print(f"Coordinates: {x}, {y} answer: {abs(x) + abs(y)}")

example_input = '''\
.#.
..#
###
'''

puzzle_input = '''\
..#....#
##.#..##
.###....
#....#.#
#.######
##.#....
#.......
.#......'''

from copy import deepcopy

def parse_input(raw_input):
    pocket_dimension = {}
    for row, line in enumerate(raw_input.split('\n')):
        for col, elem in enumerate(list(line)):
            pocket_dimension[(row, col, 0)] = elem


    return pocket_dimension


def cycle_dimension(init_dimension, cycles=6):
    dimension = deepcopy(init_dimension)
    for i in range(cycles):
        expanded_dimension = deepcopy(dimension)
        #add new points in case they don't exist
        for coords, state in dimension.items():
            for x, y, z in _generate_nearby_points(*coords):
                if not (x, y, z) in expanded_dimension:
                    expanded_dimension[(x,y,z)] = '.'

        for coords, state in expanded_dimension.items():
            dimension[coords] = det_cube_state(expanded_dimension, *coords)


    return len([e for e in dimension.values() if '#' in e])

def det_cube_state(dimension_state, x, y, z):
    surrounding_active = 0
    for targ_x, targ_y, targ_z in _generate_nearby_points(x, y, z):

        if (targ_x, targ_y, targ_z) in dimension_state and dimension_state[(targ_x, targ_y, targ_z)] == '#':
            surrounding_active += 1

    if dimension_state[(x, y, z)] == '#':
        if surrounding_active >=2 and surrounding_active <=3:
            return "#"
        else:
            return "."
    elif dimension_state[(x, y, z)] == ".":
        if surrounding_active == 3:
            return "#" #unhappy cube, wants to be active
        else:
            return "."

def _generate_nearby_points(x, y, z):
    for new_x in range(x-1, x+2, 1):
        for new_y in range(y-1, y+2, 1):
            for new_z in range(z-1, z+2, 1):
                if new_x == x and new_y == y and new_z == z:
                    continue
                yield new_x, new_y, new_z

if __name__ == '__main__':
    # init_dimension = parse_input(example_input)
    init_dimension = parse_input(puzzle_input)

    total_active = cycle_dimension(init_dimension, 6)

    print(f'Total active: {total_active}')

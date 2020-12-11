from copy import deepcopy

example_input = '''\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''


def parse_input(raw_input):
    seating_arrangement = []
    for row in raw_input.split('\n'):
        seating_row = []
        for seat in row:
            if 'L' in seat:
                seating_row.append("L")
            if '.' in seat:
                seating_row.append(".")

        seating_arrangement.append(seating_row)

    final_arrangements = {}
    for row in range(len(seating_arrangement)):
        for col in range(len(seating_arrangement[row])):
            final_arrangements[(row, col)] = seating_arrangement[row][col]

    return final_arrangements

def run_simulation_1(init_floorplan):
    not_changed = False
    running_floorplan = deepcopy(init_floorplan)

    while not not_changed:
        not_changed = True
        new_plan = deepcopy(running_floorplan)
        running_floorplan = {}

        for (row, col), seat in new_plan.items():
            adjacent_seats = [
                new_plan.get((row-1, col-1), '.'),
                new_plan.get((row, col-1), '.'),
                new_plan.get((row+1, col-1), '.'),
                new_plan.get((row-1, col), '.'),
                new_plan.get((row+1, col), '.'),
                new_plan.get((row-1, col+1), '.'),
                new_plan.get((row, col+1), '.'),
                new_plan.get((row+1, col+1), '.'),
            ]

            adjacent_occupied_count = adjacent_seats.count('#')

            if seat == '.':
                running_floorplan[(row, col)] = '.'

            elif seat == 'L' and adjacent_occupied_count == 0:
                running_floorplan[(row, col)] = '#'
                not_changed = False

            elif seat == '#' and adjacent_occupied_count >= 4:
                running_floorplan[(row, col)] = 'L'
                not_changed = False

            else:
                running_floorplan[(row, col)] = seat

    return list(running_floorplan.values()).count('#')


#################
#               #
# simulation 2  #
#               #
#################

def run_simulation_2(init_floorplan):
    not_changed = False
    running_floorplan = deepcopy(init_floorplan)

    while not not_changed:
        not_changed = True
        new_plan = deepcopy(running_floorplan)
        running_floorplan = {}

        for (row, col), seat in new_plan.items():
            adjacent_seats = [
                _seat_visible_in_direction(new_plan, row, col, -1, -1),
                _seat_visible_in_direction(new_plan, row, col, 0, -1),
                _seat_visible_in_direction(new_plan, row, col, 1, -1),
                _seat_visible_in_direction(new_plan, row, col, -1, 0),
                _seat_visible_in_direction(new_plan, row, col, 1, 0),
                _seat_visible_in_direction(new_plan, row, col, -1, 1),
                _seat_visible_in_direction(new_plan, row, col, 0, 1),
                _seat_visible_in_direction(new_plan, row, col, 1, 1),
            ]

            adjacent_occupied_count = adjacent_seats.count('#')

            if seat == '.':
                running_floorplan[(row, col)] = '.'

            elif seat == 'L' and adjacent_occupied_count == 0:
                running_floorplan[(row, col)] = '#'
                not_changed = False

            elif seat == '#' and adjacent_occupied_count >= 5:
                running_floorplan[(row, col)] = 'L'
                not_changed = False

            else:
                running_floorplan[(row, col)] = seat

    return list(running_floorplan.values()).count('#')

def _seat_visible_in_direction(cur_arrangement, start_row, start_col, x_dir, y_dir):
    seat_row = start_row
    seat_col = start_col

    while True:
        seat_row += x_dir
        seat_col += y_dir
        key = (seat_row, seat_col)
        if key not in cur_arrangement:
            return '.'

        char = cur_arrangement.get(key)
        if char == '.':
            continue
        if char == 'L':
            return 'L'
        if char == '#':
            return '#'


if __name__ == '__main__':
    # init_floorplan = parse_input(example_input)
    init_floorplan = parse_input(open("day_11_input.txt").read().strip())

    occupied_seats = run_simulation_1(init_floorplan)
    print(f"Simulation 1: {occupied_seats}")

    occupied_seats_3 = run_simulation_2(init_floorplan)
    print(f"Simulation 2: {occupied_seats_3}")

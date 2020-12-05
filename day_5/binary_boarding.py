import os

example_input = 'FBFBBFFRLR'

def parse_input(raw_data):
    return raw_data.split()

def seat_finder(seat_string: str):
    fb_count = seat_string.count('F') + seat_string.count('B')
    rl_count = seat_string.count('R') + seat_string.count('L')
    total_rows = list(range(2**(fb_count))) #2^number of 'F' and 'B'
    total_cols = list(range(2**(rl_count))) #2^number of 'R' and 'L'
    return _seat_finder(seat_string, total_rows, total_cols)

def _seat_finder(seat_string: str, cur_row_range, cur_col_range):
    if len(seat_string) > 0:

        if seat_string[0] in ['F', 'B']:
            row_midpoint = len(cur_row_range)//2
            if seat_string[0] == 'F':
                return _seat_finder(seat_string[1:], cur_row_range[:row_midpoint], cur_col_range)
            elif seat_string[0] == 'B':
                return _seat_finder(seat_string[1:], cur_row_range[row_midpoint:], cur_col_range)
        elif seat_string[0] in ['R', 'L']:
            col_midpoint = len(cur_col_range)//2
            if seat_string[0] == 'R':
                return _seat_finder(seat_string[1:], cur_row_range, cur_col_range[col_midpoint:])
            elif seat_string[0] == 'L':
                return _seat_finder(seat_string[1:], cur_row_range, cur_col_range[:col_midpoint])
    return cur_row_range[0], cur_col_range[0]


def find_all_seat_ids(all_boarding_passes):
    all_seat_ids= []
    for pass_str in all_boarding_passes:
        row, col = seat_finder(pass_str)
        seat_id = row*8 + col
        all_seat_ids.append(seat_id)

    return all_seat_ids

def find_my_seat(all_seat_ids):
    missing_seats = []
    for i in range(len(all_seat_ids)):
        cur_seat_id = all_seat_ids[i]
        if cur_seat_id - 1 not in all_seat_ids and cur_seat_id -1 not in missing_seats:
            missing_seats.append(cur_seat_id - 1)
        if cur_seat_id + 1 not in all_seat_ids and cur_seat_id +1 not in missing_seats:
            missing_seats.append(cur_seat_id + 1)

    for missing_id in missing_seats:
        if missing_id + 1 in all_seat_ids and missing_id -1 in all_seat_ids:
            return missing_id


if __name__ == '__main__':
    all_boarding_passes = parse_input(open('day_5_input.txt','r').read().strip())
    all_seat_ids = find_all_seat_ids(all_boarding_passes)
    my_seat = find_my_seat(all_seat_ids)

    print(f"My seat is: {my_seat}")

def test_seat_finder():
    row, col = seat_finder(example_input)

    assert row == 44 and col == 5

def test_find_all_seats():
    all_seat_ids =  find_all_seat_ids(parse_input(open('day_5_input.txt','r').read().strip()))

    assert len(all_seat_ids) == 850

def test_my_seat():
    all_seat_ids =  find_all_seat_ids(parse_input(open('day_5_input.txt','r').read().strip()))

    assert find_my_seat(all_seat_ids) == 623

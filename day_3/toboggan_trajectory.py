import os
import functools

example_input = '''\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#'''

def parse_map(raw_input):
    map = []
    for line in raw_input.split('\n'):
        map.append([elem for elem in line])

    return map

def traverse(map, step, stride):
    distance = len(map) #distance to travel downwords, loop iterations
    cur_col = 0 # the starting col
    cur_row = 0 # the starting row
    trees_hit = 0

    while cur_row < distance:
        if map[cur_row][cur_col] == '#':
            trees_hit += 1

        cur_col = cur_col + step if cur_col + step < len(map[cur_row]) else ((cur_col + step) % len(map[cur_row]))
        cur_row += stride
    return trees_hit


if __name__ == '__main__':
    # map = parse_map(example_input)
    map = parse_map(open('day_3_input.txt', 'r').read().strip())
    steps = [1,3,5,7,1]
    strides = [1,1,1,1,2]
    results = []
    for step, stride in zip(steps, strides):
        results.append(traverse(map, step, stride))

    print(f'Trees hit on routes : {results}')
    print(f'Answer to problem: {str(functools.reduce(lambda x, y: x*y, results))}')

def test_parse_map():
    map = parse_map(example_input)

    assert len(map) == 11
    assert len(map[0]) == 11

    assert map[0][2] == '#'
    assert map[1][2] == '.'

def test_traverse_map():
    map = parse_map(example_input)

    assert traverse(map, 3, 1) == 7
    assert traverse(map, 1, 1) == 2
    assert traverse(map, 5, 1) == 3
    assert traverse(map, 7, 1) == 4
    assert traverse(map, 1, 2) == 2

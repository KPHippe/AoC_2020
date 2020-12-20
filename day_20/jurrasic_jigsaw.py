example_input = '''\
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''
import numpy as np
from copy import deepcopy

def parse_input(raw_input):
    pieces = {}
    for block in raw_input.split('\n\n'):
        id = None
        piece = []
        for line in block.split('\n'):
            if "Tile" in line:
                id = int(line.split(' ')[-1].replace(':', ''))

            else:
                piece.append(list(line))

        pieces[id] = np.asarray(piece)
    return pieces

def assemble_puzzle(pieces):
    assembled_puzzle = {}
    for id, piece in pieces.items():
        assembled_puzzle[id] = find_compatible_pieces(id, piece, pieces)

    return assembled_puzzle

def find_compatible_pieces(target_id, target, pieces):
    compatible_pieces = {}
    for comp_id, comp_piece in pieces.items():
        if comp_id == target_id:
            continue
        compatible_list = get_compatible_edges(target, comp_piece)
        if len(compatible_list) > 0:
            compatible_pieces[comp_id] = compatible_list

    return compatible_pieces

def get_compatible_edges(target, comp):
    target_edges = {}
    target_edges['target_top'] =  target[0]
    target_edges['target_left'] = target[:,0]
    target_edges['target_right'] =  target[:,-1]
    target_edges['target_bottom'] =  target[-1]



    good_orientations = []

    for target_edge_name, target_edge in target_edges.items():
        for rot in range(0, 4, 1):
            rot_image = _rot_image(deepcopy(comp), rot)
            comp_edges = {}
            comp_edges['comp_top'] =  rot_image[0]
            comp_edges['comp_left'] =  rot_image[:,0]
            comp_edges['comp_right'] =  rot_image[:,-1]
            comp_edges['comp_bottom'] = rot_image[-1]
            for comp_edge_name, comp_edge in comp_edges.items():
                # print('\n'.join([''.join(e) for e in [target_edge, comp_edge]]))
                try:
                    if all(target_edge == comp_edge):
                        good_orientations = ((target_edge_name, (comp_edge_name, rot*90)))
                except:
                    pass # not a good orientation
                # print()
    # print(good_orientations)
    return good_orientations

def _rot_image(image, n):
    for _ in range(n):
        image = np.rot90(image)

    return image

if __name__ == '__main__':
    # pieces = parse_input(example_input)
    pieces = parse_input(open('day_20_input.txt', 'r').read().strip())

    # for id, piece in pieces.items():
    #     print(id)
    #     for line in piece:
    #         print("".join(line))

    assembled_puzzle = assemble_puzzle(pieces)
    pt1_answer = 1
    for key, compat_list in assembled_puzzle.items():
        if len(compat_list) == 2:
            pt1_answer *= key

    print(f"Product of corner id's: {pt1_answer}")

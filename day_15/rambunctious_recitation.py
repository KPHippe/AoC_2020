example_input='''\
1,3,2'''
puzzle_input = '''\
1,12,0,20,8,16'''

def parse_input(raw_input):
    return [int(e) for e in raw_input.split(',')]


def play_game(input, limit):

    last_spoken = {v: k+1 for k, v in enumerate(input[:-1])}
    prev = input[-1]
    turn = len(input)

    #change this value to get pt1, pt2
    while turn < limit:
        cur_word = turn - last_spoken[prev] if prev in last_spoken else 0
        last_spoken[prev] = turn
        prev = cur_word
        turn += 1

    return prev

if __name__ == '__main__':
    # input = parse_input(example_input)
    input = parse_input(puzzle_input)

    last_spoken = play_game(input, 2020)
    print(f"Part 1: {last_spoken}")

    last_spoken = play_game(input, 30000000)
    print(f"Part 2: {last_spoken}")

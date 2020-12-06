import os

example_input = '''\
abc

a
b
c

ab
ac

a
a
a
a

b'''

def parse_input(raw_data):
    group_data = raw_data.split("\n\n")
    parsed_group_data = []
    for group in group_data:
        individuals_answers = []
        for ind_answers in group.split('\n'):
            individuals_answers.append([e for e in ind_answers])

        parsed_group_data.append(individuals_answers)
    return parsed_group_data

def find_groups_unique_answers(group_data):
    #pt1
    groups_unique_answers = set()
    for all_answer in group_data:
        for answer in all_answer:
            groups_unique_answers.add(answer)
    return len(groups_unique_answers)

def find_common_group_answers(group_data):
    #pt2
    answer_counts = {}
    common_answers = 0
    for ind_answer in group_data:
        for answer in ind_answer:
            if answer in answer_counts.keys():
                answer_counts[answer] += 1
            else:
                answer_counts[answer] = 1

    for answer_field, count in answer_counts.items():
        if count == len(group_data):
            common_answers += 1
    return common_answers

def find_total_unique_answers(all_group_data):
    #pt1
    total = 0
    for group_answers in all_group_data:
        total += find_groups_unique_answers(group_answers)
    return total

def find_total_common_answers(all_group_data):
    #pt2
    total = 0
    for group_answers in all_group_data:
        total += find_common_group_answers(group_answers)
    return total


if __name__ == '__main__':
    # group_data = parse_input(example_input)
    group_data = parse_input(open('day_6_input.txt', 'r').read().strip())


    total_unique = find_total_unique_answers(group_data)
    total_common = find_total_common_answers(group_data)

    print(f"Total unique answers: {total_unique}")
    print(f"Total common answers: {total_common}")

def test_group_unique_answers():
    group_data = parse_input(example_input)

    assert find_groups_unique_answers(group_data[0]) == 3
    assert find_groups_unique_answers(group_data[1]) == 3
    assert find_groups_unique_answers(group_data[-1]) == 1

def test_total_unique_answers():
    group_data = parse_input(example_input)

    assert find_total_unique_answers(group_data) == 11

def test_total_common_answers():
    group_data = parse_input(example_input)

    assert find_total_common_answers(group_data) == 6

def test_group_common_answers():
    group_data = parse_input(example_input)

    assert find_common_group_answers(group_data[0]) == 3
    assert find_common_group_answers(group_data[1]) == 0
    assert find_common_group_answers(group_data[-1]) == 1

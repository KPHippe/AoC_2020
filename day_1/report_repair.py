import os
import sys

example_input = '''\
1721
979
366
299
675
1456'''

def find_two_2020(report):
    target = 2020

    for i in range(len(report)):
        for j in range(len(report)):
            if report[i] + report[j] == target:
                return i, j

def find_three_2020(report):
    target = 2020

    for x in range(len(report)):
        for y in range(len(report)):
            for z in range(len(report)):

                if report[x] + report[y] + report[z] == target:
                    return x, y, z
def test_find_two():
    report = [int(e) for e in example_input.split('\n')]
    ind_1, ind_2 = find_two_2020(report)
    assert report[ind_1] * report[ind_2] == 514579

def test_find_three():
    report = [int(e) for e in example_input.split('\n')]
    ind_1, ind_2, ind_3 = find_three_2020(report)
    assert report[ind_1] * report[ind_2]* report[ind_3] == 241861950



if __name__ == '__main__':
    report = [int(e) for e in open('day_1_input.txt', 'r').read().strip().split('\n')]
    ind_1, ind_2 = find_two_2020(report)
    ind_1, ind_2, ind_3 = find_three_2020(report)

    print(f'Two: {str(report[ind_1] * report[ind_2])}')
    print(f'Three: {str(report[ind_1] * report[ind_2]* report[ind_3])}')

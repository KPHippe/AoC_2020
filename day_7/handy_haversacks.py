
from collections import deque

example_input = '''\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.'''

example_input2 = '''\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''

counter = 0
def parse_input(raw_data):
    return raw_data.split('.\n')

def establish_rules(raw_rules):
    rules_graph = {}
    for rule in raw_rules:
        object, contents = rule.split('contain')
        object = object.split(' bags')[0]
        bag_content = {}
        try:
            for raw_bag in contents.split(','):
                bag_name = raw_bag.split('bag')[0].strip()[2:]
                bag_count = int(raw_bag[1])
                bag_content[bag_name] = bag_count

        except ValueError: #no contents
            if 'no other bags' in contents:
                pass
            else:
                bag_name = contents.strip()[2:]
                bag_count = int(contents[1])
                bag_content[bag_name] = bag_count

        rules_graph[object] = bag_content
    return rules_graph

def find_all_gold_holders(rules_graph, target):
    count = 0
    for bag_name in rules_graph:
        if hold_gold(rules_graph, bag_name, target):
            count +=1

    return count

def hold_gold(rules, cur_bag, target):
    if target in rules[cur_bag]:
        return True
    for other_bags in rules[cur_bag]:
        if hold_gold(rules, other_bags, target):
            return True
    return False

def count_all_gold_holds(rules_graph, target):
    global counter
    for bag_name, count in rules_graph[target].items(): #dark olive, violet plum
        for _ in range(count):
            # print(bag_name)
            counter += 1
            count_contents(rules_graph, bag_name)
    return counter


def count_contents(rules_graph, cur_bag):
    global counter
    for bag_name, count in rules_graph[cur_bag].items():
        for _ in range(count):
            # print(bag_name)
            counter += 1
            if len(rules_graph[bag_name]) != 0:
                count_contents(rules_graph, bag_name)

if __name__ == '__main__':
    # raw_rules = parse_input(example_input2)
    raw_rules = parse_input(open('day_7_input.txt', 'r').read().strip())
    rules_graph = establish_rules(raw_rules)

    total_containers = find_all_gold_holders(rules_graph, 'shiny gold')
    print(f'Total ways to reach shiny gold: {total_containers}')

    total_bags = count_all_gold_holds(rules_graph, 'shiny gold')
    print(f'Total bags to contain shiny gold: {total_bags}')

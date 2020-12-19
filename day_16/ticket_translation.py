example_input= '''\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

import re
def parse_input(raw_input):
    rules = {}
    my_ticket = None
    nearby_tickets = []
    raw_input = raw_input.split('\n\n')
    for line in raw_input[0].split('\n'):
        id, rule = line.split(': ')
        rules[id] = []
        for rule_range in rule.split(' or '):
            low, high = rule_range.split('-')
            rules[id].append(range(int(low), int(high) + 1, 1))


    my_ticket = [int(e) for e in raw_input[1].split(':')[-1].split(',')]

    for line in raw_input[2].split('\n'):
        if 'tickets' in line:
            continue
        key = tuple([int(e) for e in line.split(',')])
        nearby_tickets.append(key)

    return rules, my_ticket, nearby_tickets

def scan_nearby_tickets(ticket_rules, nearby_tickets):
    invalid_tickets = []
    valid_tickets = []
    for ticket_vals in nearby_tickets:
        valid = True
        for val in ticket_vals:
            if not _validate_ticket(ticket_rules, val):
                invalid_tickets.append(val)
                valid = False
        if valid:
            valid_tickets.append(ticket_vals)

    return sum(invalid_tickets), valid_tickets

def _validate_ticket(ticket_rules, class_val):
    for rule_name, constraints in ticket_rules.items():
        for constraint in constraints:
            if class_val in constraint:
                return True

    return False


def find_classes(ticket_rules, valid_tickets):
    overall_valid_fields = {}
    for ticket in valid_tickets:
        valid_fields = {} #keys are the rule name in the rules dict, values are the fields that are valid_fields
        for field, rules in ticket_rules.items():
            valid_indices = validate_field(field, rules, ticket)
            if len(valid_indices) > 0:
                if field in overall_valid_fields:
                    new_valid_indices = set()
                    for corr_field in overall_valid_fields[field]:
                        if corr_field in valid_indices:
                            new_valid_indices.add(corr_field)

                    overall_valid_fields[field] = new_valid_indices
                else:
                    overall_valid_fields[field] = valid_indices

    while (sum([len(v) for k,v in overall_valid_fields.items()]) != len(overall_valid_fields.keys())):
        cur_one_length = []
        for field, valid_set in overall_valid_fields.items():
            if len(valid_set) == 1:
                val = list(valid_set)[0]
                cur_one_length.append((field, val))

        for (field, val) in cur_one_length:
            for target_field in overall_valid_fields:
                if not field in target_field:
                    try:
                        overall_valid_fields[target_field].remove(val)
                    except:
                        pass

    return overall_valid_fields

def validate_field(field, rule, ticket):
    res = set()
    for i, val in enumerate(ticket):
        for val_range in rule:
            # print(val, val_range, val in val_range)
            if val in val_range:
                res.add(i)

    return res


if __name__ == '__main__':
    # rules, my_ticket, nearby_tickets = parse_input(example_input)
    rules, my_ticket, nearby_tickets = parse_input(open('day_16_input.txt', 'r').read().strip())

    total_invalid_vals, valid_tickets = scan_nearby_tickets(rules, nearby_tickets)
    print(f"Invalid ticket sum: {total_invalid_vals}")

    valid_fields = find_classes(rules, valid_tickets)
    product_answer = 1
    for field, index in valid_fields.items():
        if 'departure' in field:
            arr_index = list(index)[0]
            product_answer *= my_ticket[arr_index]

    print(f"My ticket product: {product_answer}")

import os

example_input = '''\
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc'''


def determine_validity_occurences(password_rule, password):
    for char, occurence_range in password_rule.items():
        min, max = occurence_range[0], occurence_range[-1] + 1
        if password.count(char) in range(min, max):
            return True
        return False

def determine_validity_position(password_rule, password):
    for char, occurence_positions in password_rule.items():
        requirements_met = False
        occurences = [i+1 for i in range(len(password)) if password[i] == char]
        for char_occurence in occurences:
            if char_occurence in occurence_positions and not requirements_met:
                requirements_met = True
            elif char_occurence in occurence_positions and requirements_met:
                # we have our exclusive case met, return False
                return False
        return requirements_met

def parse_input(raw_data):
    for line in raw_data.split("\n"):
        rule, password = line.split(':')
        rule = {rule.split(' ')[-1]: [int(e) for e in rule.split(' ')[0].split('-')]}
        password = password.strip()

        yield rule, password

def find_good_passwords(raw_data):
    good_count = 0
    for rule, password in parse_input(raw_data):
        if determine_validity_occurences(rule, password):
            good_count += 1

    print(f"Good passwords, occurence rules: {good_count}")

    good_count = 0
    for rule, password in parse_input(raw_data):
        if determine_validity_position(rule, password):
            good_count += 1

    print(f"Good passwords, positional rules: {good_count}")


if __name__ == '__main__':
    # find_good_passwords(example_input)
    find_good_passwords(open('day_2_input.txt').read().strip())


def test_parse_input():
    for rule, password in parse_input(example_input):
        assert isinstance(rule, type({}))
        assert isinstance(password, str)

        for k, occurence_range in rule.items():
            assert isinstance(k, str)
            assert isinstance(occurence_range, type([]))

def test_determine_validity_occurences():
    #true
    rule = {'a': [1,3]}
    password = 'abcde'
    assert determine_validity_occurences(rule, password)

    #not true
    rule = {'f': [1,3]}
    password = 'abcde'
    assert not determine_validity_occurences(rule, password)

def test_determine_validity_positions():
    #true
    rule = {'a': [1,3]}
    password = 'abcde'
    assert determine_validity_position(rule, password)

    #not true
    rule = {'b': [1,3]}
    password = 'cdefg'
    assert not determine_validity_position(rule, password)

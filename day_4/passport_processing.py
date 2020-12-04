import re
import json

example_input = '''\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719'''

all_fields = ['byr',
              'iyr',
              'eyr',
              'hgt',
              'hcl',
              'ecl',
              'pid',
              'cid'
              ]

def parse_input(raw_data):
    all_passports = []
    for line in raw_data.split('\n\n'):
        passport_data = {}
        fields = line.split()
        for field in fields:
            key, value = field.split(':')
            passport_data[key] = value
        all_passports.append(passport_data)
    return all_passports

def validate_fields(field, data):
    valid = True
    if 'byr' in field:
        try:
            data = int(data)
            if data < 1920 or data > 2002:
                valid = False
        except:
            valid = False

    elif 'iyr' in field:
        try:
            data = int(data)
            if data < 2010 or data > 2020:
                valid = False
        except:
            valid = False

    elif 'eyr' in field:
        try:
            data = int(data)
            if data < 2020 or data > 2030:
                valid = False
        except:
            valid = False

    elif 'hgt' in field:
        if 'cm' in data:
            try:
                data = int(data[:-2])
                if data < 150 or data > 193:
                    valid = False
            except:
                valid = False

        elif 'in' in data:
            try:
                data = int(data[:-2])
                if data < 59 or data > 76:
                    valid = False
            except:
                valid = False
        else:
            valid = False

    elif 'hcl' in field:
        if re.match('^#(?:[0-9a-fA-F]{3}){1,2}$', data) == None:
            valid = False

    elif 'ecl' in field:
        if data not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False

    elif 'pid' in field:
        if len(data) != 9:
            valid = False
        try:
            int_data = int(data)
        except:
            valid = False

    elif 'cid' in field:
        pass

    else:
        valid = False


    return valid


def validate_passport(passport, optional_fields=None):
    valid = True
    for field in all_fields:
        if field not in passport and field not in optional_fields:
            return False
        elif field not in passport and field in optional_fields:
            continue
        else:
            if valid:
                valid = validate_fields(field, passport[field])
            else:
                return valid

    return valid

def validate_all_passports(all_passports, optional_fields=None):
    valid_passports = 0
    for passport in all_passports:
        if validate_passport(passport, optional_fields):
            valid_passports += 1
    return valid_passports

if __name__ == '__main__':
    # all_passports = parse_input(example_input)
    all_passports = parse_input(open('day_4_input.txt', 'r').read().strip())

    optional_fields = ['cid']
    valid_passports = validate_all_passports(all_passports, optional_fields)

    print(f'Valid passports: {valid_passports}')

#TODO: Add testing for validate fields
def test_validate_one_passport():
    all_passports = parse_input(example_input)

    assert not validate_passport(all_passports[0])
    assert validate_passport(all_passports[5])

def test_validate_all_passports():
    all_passports = parse_input(example_input)

    assert validate_all_passports(all_passports, ['cid']) == 4

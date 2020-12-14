example_input = '''\
939
7,13,x,x,59,x,31,19'''

from functools import reduce
import operator

def parse_input(raw_data):
    arrival = None
    bus_ids = []
    for i, line in enumerate(raw_data.split('\n')):
        if i == 0:
            arrival = int(line)
        else:
            for bus_id in line.split(","):
                try:
                    bus_ids.append(int(bus_id))
                except:
                    bus_ids.append(None)
    return arrival, bus_ids

def find_soonest_bus(arrival, bus_ids):
    cur_time = arrival
    on_bus = False
    while not on_bus:
        for bus_schedule in bus_ids:
            if bus_schedule is None:
                 continue
            if cur_time in range(0, cur_time+1, bus_schedule):
                on_bus = True
                return cur_time, bus_schedule

        cur_time += 1

def find_consecutive_busses(bus_ids):
    rules = generate_rules(bus_ids)
    step = max([e for e in bus_ids if not e is None])
    cur_time = step
    while True:
        # if cur_time % bus_ids[0] == 0:
        # if cur_time in range(0, cur_time + 1, bus_ids[0]):
        valid_step = True
        for i, rule in enumerate(rules):
            if not rule is None:
                if not ((cur_time + rule) % bus_ids[i]) == 0:
                    valid_step = False
                    break

        if valid_step:
            return cur_time + (rules[0])
        cur_time += step

def generate_rules(bus_ids):
    rules = []
    max_index = bus_ids.index(max([e for e in bus_ids if not e is None]))
    for i, id in enumerate(bus_ids):
        if not id is None:
            rules.append(i- max_index)
        else:
            rules.append(None)
    return rules

 #optimized solution with Chinese Remainder Theorum
def CRT(raw_busses):
    # Suppose bus K appears at index I in the list.
    # K should depart at time T+I. i.e. T+I should be a multiple of K.
    # T+I % K == 0
    # T % K == -I
    # T % K == (K-(I%K))%K (want 0<=RHS<K)

    # Chinese remainder theorem: Let N be the product of the bus IDs in our input.
    # There is exactly one T <N satisfying the constraints.

    constraints = []
    N = 1
    for i,b in enumerate(raw_busses):
        if b!='x':
            b = int(b)
            i %= b
            constraints.append(((b-i)%b,b))
            N *= b

    print(constraints)
    ans = 0
    # x % b = i
    for (i,b) in constraints:
        NI = N/b
        # NI is the product of the *other* bus IDs
        # If we add a multiple of NI to T, it won't affect when the other buses arrive modulo T,
        # since NI is a multiple of each other bus ID.
        # Is there a multiple of NI we can add to T so that T%b==i? Yes!
        # We want to find a multiple of NI s.t. (a*NI)%b == i
        # First find MI s.t. (MI*NI)%b == 1
        # Then (i*MI*NI)%b == i
        assert gcd(NI,b) == 1
        mi = mod_inverse(NI, b)
        assert mi == mod_inverse(NI, b)
        assert (mi*NI)%b == 1
        assert (i*mi*NI)%b == i
        for_b = i*mi*NI
        assert for_b%b == i
        assert for_b%NI == 0
        ans += for_b
        #print(i,ni,mi,b)

    ans %= N
    for i,b in constraints:
        assert ans%b == i

    return int(ans)

def gcd(x,y):
    if x==0:
        return y
    return gcd(y%x, x)

def mod_inverse(a, m):
    return mod_pow(a%m, m-2, m)

def mod_pow(b, e, mod):
    if e==0:
        return 1
    elif e%2==0:
        # If E is even, a**E = (a^2)^(E/2)
        return mod_pow((b*b)%mod, e/2, mod)
    else:
        return (b*mod_pow(b,e-1,mod))%mod

if __name__ == '__main__':
    # arrival, busses = parse_input(example_input)
    arrival, busses = parse_input(open('day_13_input.txt', 'r').read().strip())

    bus_time, id = find_soonest_bus(arrival, busses)
    print(f'Time: {bus_time}, id: {id} answer: {str((bus_time-arrival)* id)}')

    #Dont run this, it is very slow
    # consecutive_time = find_consecutive_busses(busses)
    # print(f'Consecutive busses: {consecutive_time}')


    #come back to this one later!
    raw_busses = open('day_13_input.txt', 'r').read().split('\n')[1].strip().split(',')
    raw_example = example_input.split('\n')[1].strip().split(',')
    print(raw_busses)
    print(raw_example)
    # consecutive_time = CRT(raw_example)
    consecutive_time = CRT(raw_busses)
    print(f"Consecutive time: {consecutive_time}")

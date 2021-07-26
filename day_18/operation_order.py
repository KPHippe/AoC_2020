example_input = '''\
1 + (2 * 3) + (4 * (5 + 6))
'''


def eval(equation, precedence):
    equation = equation.strip().split(" ")
    # print(equation)
    operators, postfix = [], []
    # convert to postfix then evaluate
    for token in equation:
        if str.isdigit(token):
            postfix.append(token)
        elif token == "(":
            operators.append(token)
        elif token == ")":
            op = operators.pop()
            while op != "(":
                postfix.append(op)
                op = operators.pop()
        else:
            while len(operators) > 0 and precedence[operators[-1]] >= precedence[token]:
                postfix.append(operators.pop())

            operators.append(token)

    while len(operators) > 0:
        postfix.append(operators.pop())

    # print(postfix)

    # eval postfix
    operands = {"*": _multiply,
                "+": _add,
                "-": _subtract
                }
    operands = []
    for token in postfix:
        if str.isdigit(token):
            operands.append(int(token))
        else:
            lhs = operands.pop()
            rhs = operands.pop()
            operands.append(small_evaluate(rhs, lhs, token))

    return int(operands[0])


def small_evaluate(rhs, lhs, op):
    operands = {"*": _multiply,
                "+": _add,
                "-": _subtract
                }
    return str(operands[op](int(rhs), int(lhs)))


def _multiply(rhs, lhs):
    return rhs * lhs


def _add(rhs, lhs):
    return rhs + lhs


def _subtract(rhs, lhs):
    return rhs - lhs


if __name__ == '__main__':
    p1_precedence = {"+": 2,
                     "*": 2,
                     "(": 1
                     }
    p2_precedence = {"+": 3,
                     "*": 2,
                     "(": 1
                     }


    # example_input = example_input.replace("(", "( ")
    # example_input = example_input.replace(")", " )")
    # print(eval(example_input, precedence))

    input = open("day_18_input.txt").readlines()
    total = 0
    for line in input:
        line = line.replace("(", "( ")
        line = line.replace(")", " )")
        total += eval(line, p2_precedence)

    print(f"Result: {total}")

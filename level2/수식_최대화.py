from itertools import permutations
import re
def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def calculate(exp, op):
    array=re.split('([^0-9])',exp)
    for o in op:
        stack = []
        while len(array) != 0:
            tmp = array.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array = stack
    return abs(int(array[0]))


def solution(expression):
    op = list(permutations(['+', '-', '*'], 3))
    result = []
    for i in op:
        result.append(calculate(expression, i))
    return max(result)
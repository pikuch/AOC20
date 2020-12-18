# AOC20 day 18
from collections import deque


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def operation(x, oper, y):
    if oper == "+":
        return x+y
    elif oper == "*":
        return x*y
    else:
        return ""


def evaluate(expr):
    expr = expr.replace("(", "( ").replace(")", " )")
    items = expr.split()
    stack = [deque()]
    for item in items:
        if item in "0123456789":
            if len(stack[-1]):
                stack[-1].append(operation(int(item), stack[-1].pop(), stack[-1].pop()))
            else:
                stack[-1].append(int(item))
        elif item in "*+":
            stack[-1].append(item)
        elif item == "(":
            stack.append(deque())
        elif item == ")":
            ret = stack[-1].pop()
            stack.pop()
            if len(stack[-1]):
                stack[-1].append(operation(ret, stack[-1].pop(), stack[-1].pop()))
            else:
                stack[-1].append(ret)
    return stack[-1].pop()





def run():
    data = load_data("Day18.txt")
    expressions = data.splitlines()
    print(sum(map(evaluate, expressions)))
    #print(sum(map(evaluate_plus, expressions)))

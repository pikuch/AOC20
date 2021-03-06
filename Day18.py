# AOC20 day 18
from collections import deque


def load_data(f_name):
    with open(f_name, "r") as f:
        data_read = f.read()
    return data_read


def operation(x, op, y):
    if op == "+":
        return x+y
    elif op == "*":
        return x*y
    else:
        print(f"Invalid operation: {x}{op}{y}")
        exit(1)


def eval_stack_top(stack, new_item):
    if len(stack):
        stack.append(operation(new_item, stack.pop(), stack.pop()))
    else:
        stack.append(new_item)


def evaluate(expr):
    expr = expr.replace("(", "( ").replace(")", " )")
    items = expr.split()
    stack = [deque()]
    for item in items:
        if item in "0123456789":
            eval_stack_top(stack[-1], int(item))
        elif item in "*+":
            stack[-1].append(item)
        elif item == "(":
            stack.append(deque())
        elif item == ")":
            ret = stack[-1].pop()
            stack.pop()
            eval_stack_top(stack[-1], ret)
    return stack[-1].pop()


def eval_stack_top_plus(stack, new_item):
    if len(stack):
        if stack[-1] == "+":
            stack.append(operation(new_item, stack.pop(), stack.pop()))
        else:
            stack.append(new_item)
    else:
        stack.append(new_item)


def eval_leftovers(stack):
    while len(stack) > 1:
        stack.append(operation(stack.pop(), stack.pop(), stack.pop()))


def evaluate_plus(expr):
    expr = expr.replace("(", "( ").replace(")", " )")
    items = expr.split()
    stack = [deque()]
    for item in items:
        if item in "0123456789":
            eval_stack_top_plus(stack[-1], int(item))
        elif item in "*+":
            stack[-1].append(item)
        elif item == "(":
            stack.append(deque())
        elif item == ")":
            eval_leftovers(stack[-1])
            ret = stack[-1].pop()
            stack.pop()
            eval_stack_top_plus(stack[-1], ret)
    eval_leftovers(stack[-1])
    return stack[-1].pop()


def run():
    data = load_data("Day18.txt")
    expressions = data.splitlines()
    print(sum(map(evaluate, expressions)))  # 7293529867931
    print(sum(map(evaluate_plus, expressions)))  # 60807587180737

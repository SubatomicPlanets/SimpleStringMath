import re

def shunting_yard(expression):
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # Operator precedence
    output_queue = []
    operator_stack = []

    tokens = re.findall(r'\d+|\S', expression)
    for token in tokens:
        if token.isdigit():
            output_queue.append(token)
        elif token in operators:
            while (operator_stack and
                   operator_stack[-1] != '(' and
                   operators[token] <= operators[operator_stack[-1]]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue

def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)
    if stack:
        return stack.pop()
    else:
        return None

def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    elif operator == '^':
        return operand1 ** operand2
    
def evaluate(sentence):
    return evaluate_postfix(shunting_yard(sentence))

  
#run the evaluate function to get an output
    

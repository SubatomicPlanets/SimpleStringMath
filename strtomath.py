import re

operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  #order of operations
constants = {"pi":"3.141592", "e":"2.71828"}          #add custom constants here

def shunting_yard(expression):  
    #infix to postfix function. uses the shunting yard algorithm 
    output_queue = []
    operator_stack = []
    tokens = re.findall(r'(?<=[ \(\)\+\-\*\/])-?\d+\.?\d*|(?<=[ \(\)\+\-\*\/])-?[a-zA-Z]+|\S', " "+expression)  #unclean code to find math expressions, but it works...
    for token in tokens:
        if token.replace("-", "") in constants:  #unclean code to allow negative constants, but it works...
            is_negative = token[0] == "-"
            token = constants[token.replace("-", "")]
            if is_negative: 
                token = "-" + token
        if re.match(r'-?\d+\.?\d*', token):
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
    #figures out what to do with specific numbers
    stack = []
    for token in expression:
        if re.match(r'-?\d+\.?\d*', token):
            stack.append(float(token))  
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(token, operand1, operand2)
            stack.append(result)
    if stack:
        return stack.pop()
    else:
        return None

def perform_operation(operator, operand1, operand2):  
    #do the actual math
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
    #this is the main function. call this function and pass it a string to get the output.
    return evaluate_postfix(shunting_yard(sentence))
    
##use like this:
##
##while True:
##    print(evaluate(input("You: ")))

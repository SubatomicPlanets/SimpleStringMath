import re

numbers = {'zero': (1, 0), 'one': (1, 1), 'two': (1, 2), 'three': (1, 3), 'four': (1, 4), 'five': (1, 5),
    'six': (1, 6), 'seven': (1, 7), 'eight': (1, 8), 'nine': (1, 9), 'ten': (1, 10), 'eleven': (1, 11), 'twelve': (1, 12),
    'thirteen': (1, 13), 'fourteen': (1, 14), 'fifteen': (1, 15), 'sixteen': (1, 16), 'seventeen': (1, 17), 'eighteen': (1, 18),
    'nineteen': (1, 19), 'twenty': (1, 20), 'thirty': (1, 30), 'forty': (1, 40), 'fifty': (1, 50), 'sixty': (1, 60),
    'seventy': (1, 70), 'eighty': (1, 80), 'ninety': (1, 90), 'hundred': (100, 0), 'thousand': (1000, 0), 'million': (1000000, 0),
    'billion': (1000000000, 0), 'trillion': (1000000000000, 0)}

operators = {"+": 1, "-": 1, "*": 2, "/": 2, "%":2, "^": 3}  #order of operations

#constants and words that should be replaced with symbols
replacers = {"pi":"3.141592", "e":"2.71828","plus":"+","minus":"-","divided by":"/","multiplied by":"*",
            "times":"*","to the power of":"^","power":"^"}

def word_to_number_converter(sentence):
    current = 0
    num = 0
    nums = []
    is_num = False
    
    for r in replacers:
        sentence = re.sub(r"(?<![a-z])"+r+"(?![a-z])", replacers[r], sentence)

    for word in re.findall(r"[a-z]+|\-?\d+\.?\d*|\S", sentence):
        if word in ["and"]:  #words to ignore
            continue
        elif word not in numbers:
            if is_num == True:
                nums.append(str(num+current))
            nums.append(word)
            num = 0
            current = 0
            is_num = False
            continue
        is_num = True
        scale, increment = numbers[word]
        current = current * scale + increment
        if scale > 100:
            num += current
            current = 0

    if is_num == True:
        nums.append(str(num+current))
    return " ".join(nums)

def shunting_yard(expression):
    #infix to postfix function. uses the shunting yard algorithm. example:  5+4*(5-4)  ->  5454-*+
    output_queue = []
    operator_stack = []
    tokens = re.findall(r"(?<=[ \(\)\+\-\*\/\%])-?\d+\.?\d*|(?<=[ \(\)\+\-\*\/\%])-?[a-zA-Z]+|\S", " "+expression)  #unclean code to find math expressions, but it works...
    for token in tokens:
        if re.match(r"-?\d+\.?\d*", token):
            output_queue.append(token)
        elif token in operators:
            while (operator_stack and
                   operator_stack[-1] != "(" and
                   operators[token] <= operators[operator_stack[-1]]):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == "(":
            operator_stack.append(token)
        elif token == ")":
            while operator_stack and operator_stack[-1] != "(":
                output_queue.append(operator_stack.pop())
            if operator_stack and operator_stack[-1] == "(":
                operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue

def evaluate_postfix(expression):
    #calls the perform_math function with specific operators and numbers
    stack = []
    for token in expression:
        if re.match(r"-?\d+\.?\d*", token):
            stack.append(float(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_math(token, operand1, operand2)
            stack.append(result)
    if stack:
        return stack.pop()
    else:
        return ""  #returns "" if there is no math in the input sentence

def perform_math(operator, operand1, operand2):
    #do the actual math
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "^":
        return operand1 ** operand2
    elif operator == "%":
        return operand1 % operand2

def evaluate(sentence):
    #this is the main function. call this function and pass it a string to get the output.
    sentence = sentence.lower().strip()
    processed_sentence = word_to_number_converter(sentence)  #"one hundred and seventy minus (56*PI)"  ->  "170 - (56*3.141592)"
    postfix = shunting_yard(processed_sentence)              #"170 - (56*pi)"  ->  "170 56 3.141592 * -"
    result = evaluate_postfix(postfix)                   #"170 56 3.141592 * -"  ->  "-5.929152000"
    return result

##use like this:
##
##while True:
##    print(evaluate(input("You: ")))

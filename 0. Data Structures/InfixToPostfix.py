#Infix to Postfix
class stack:

    def __init__(self):
        self.stack =[]

    def isEmpty(self):
        return len(self.stack) ==0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise Exception("pop() called on empty stack")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("peek() called on empty stack")

def prec(c):

    if c == '+' or c == '-':
        return 1
    elif c == '*' or c == '/':
        return 2
    else:
        return -1


def infix_to_postfix(expression):

    result = []
    operator = stack()

    for i in range(len(expression)):

        c = expression[i]

        if c.isalnum():
            result.append(c)
        elif c == '(':
            operator.push(c)
        elif c == ')':
            while operator and operator[-1]!='(':
                result.append(operator.pop())
            operator.pop()
        else:
            while not operator.isEmpty() and (prec(c)<=prec(operator.peek())):
                result.append(operator.pop())
            operator.push(c)

    while not operator.isEmpty():
        result.append(operator.pop())

    return ''.join(result)




expression = input()
result = infix_to_postfix(expression)
print(result)
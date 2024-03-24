# Evaluate Reverse Polish Notation

def evalRPN(token):

    stack = []

    for i in token:
        if i.isalnum():
            stack.append(int(i))
        else:
            if i == '+':
                stack.append(stack.pop()+stack.pop())
            if i == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            if i == '*':
                stack.append(stack.pop()*stack.pop())
            if i == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(b/a)

    return stack.pop()


token = list(map(str, input().split()))
print(evalRPN(token))
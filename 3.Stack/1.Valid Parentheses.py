'''
An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
'''

def isValid(str):
    map = {")": "(", "}": "{", "]": "["}
    stack =[]

    for s in str:
        if s in map:
            if stack and stack[-1]==map[s]:
                stack.pop()
            else:
                return False
        else:
            stack.append(s)

    return not stack

str = input()
print(isValid(str))

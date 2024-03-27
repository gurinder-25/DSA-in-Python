#Daily Temperature

def daily(temperature):

    result = [0] * len(temperature)
    stack = []

    for i, t in enumerate(temperature):
        while stack and t > stack[-1][0]:
            stackT, stackI = stack.pop()
            result[stackI] = i - stackI
        stack.append([t, i])

    return result

temperature = list(map(int, input().split()))
print(daily(temperature))

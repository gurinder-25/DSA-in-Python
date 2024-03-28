#Car Fleet

def carfleet(target, position, speed):

    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)
    stack = []

    for p, s in pairs:
        stack.append((target - p)/s)
        if len(stack)>=2 and stack[-1]<=stack[-2]:
            stack.pop()

    return len(stack)



target = int(input())
position = list(map(int, input().split()))
speed = list(map(int, input().split()))

print(carfleet(target, position, speed))
def maxArea(height):
    container = 0
    l, r = 0, len(height) - 1

    while (l < r):
        area1 = min(height[l], height[r])
        container = max(container, area1 * (r - l))

        if (height[l] > height[r]):
            r -= 1
        else:
            l += 1

    return container


heights = list(map(int, input().split()))
print(maxArea(heights))
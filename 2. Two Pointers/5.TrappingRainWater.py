def trap(height):
    l = 0
    r = len(height) - 1
    count = 0
    Lmax = height[l]
    Rmax = height[r]

    while l < r:
        if Lmax < Rmax:
            l += 1
            Lmax = max(Lmax, height[l])
            count += Lmax - height[l]
        else:
            r -= 1
            Rmax = max(Rmax, height[r])
            count += Rmax - height[r]

    return count


heights = list(map(int, input().split()))
print(trap(heights))
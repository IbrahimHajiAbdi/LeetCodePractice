import time

def maxArea(height):
    maxVol = 0
    l, r = 0, len(height) - 1
    
 
    while l < r:
        vol = min(height[l], height[r]) * (r - l)
        if vol > maxVol:
            maxVol = vol
        if height[r] < height[l]:
            r -= 1
        else: l += 1 
    return maxVol

start = time.time()
print(maxArea([1,8,6,2,5,4,8,3,7]))
end = time.time()
print(end - start)
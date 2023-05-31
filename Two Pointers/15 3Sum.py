# def threeSum(nums):
#     firstPtr, secondPtr, thirdPtr = 0, 0, 0
#     ans = []
#     for i in range(len(nums)-2):
#         if nums[firstPtr+i] + nums[secondPtr+i+1] + nums[thirdPtr+i+2] == 0:
#             ans.append([nums[firstPtr+i], nums[secondPtr+i+1], nums[thirdPtr+i+2]])
#     return ans
def threeSum(nums):
    def twoSum(nums, target):
        d = {}
        ans = []
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = num
            if ((target - num) in d):
                ans.append([d[target - num], nums[i]])

        return ans

    ans = []
    for i in range(len(nums)):
        arr = twoSum(nums[i+1:], 0-nums[i])
        if not arr: continue
        for j in arr:
            j.append(nums[i]); j = sorted(j)
            if not ans: ans.append(j)
            contains = False
            for k in ans:
                if j == k:
                    contains = True
            if not contains:
                ans.append(j)
    return ans
            
            
print(threeSum([1,2,-2,-1]))


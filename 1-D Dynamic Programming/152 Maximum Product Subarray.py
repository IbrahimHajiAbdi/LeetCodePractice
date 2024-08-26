from typing import List
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        res = float('-inf')
        subArrays = []
        l, r = 0, 1
        for num in nums:
            if num == 0:
                subArrays.append(nums[l:r-1])
                l = r
            r += 1
        subArrays.append(nums[l:r-1])
        if not subArrays:
            subArrays.append(nums)
        for i in subArrays:
            res = max(res, self.maxProductSubArray(i))
        # print(subArrays)
        return max(nums) if res < max(nums) else res
        
    def maxProductSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] * nums[1] if nums[0] * nums[1] > max(nums) else max(nums)
        res = float('-inf')
        product = nums[0]
        for i in range(1, len(nums)):
            product = product * nums[i]
            res = max(res, product)
        for i in range(len(nums)):
            product = product // nums[i]
            res = max(res, product)
        return max(nums) if max(nums) > res else res
        
sol = Solution()
print(sol.maxProduct([2,3,-2,4]), "answer = 6") 
print(sol.maxProduct([-2,4,5,0,6,5]), "answer = 30") 
print(sol.maxProduct([0,0,0,0,0]), "answer = 0") 
print(sol.maxProduct([0,1,0,1,0]), "answer = 1") 
print(sol.maxProduct([-2,3,-4]), "answer = 24") 

from typing import List


def findMin(nums: List[int]) -> int:
    deflection = len(nums) - 1
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            deflection = i
            break
    if deflection != len(nums) - 1:
        return nums[deflection + 1]
    else:
        return nums[0]
        

print(findMin([11,13,15,17]))  
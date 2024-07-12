from typing import List


def search(nums: List[int], target: int) -> int: 
    if len(nums) == 1:
        return -1 if nums[0] != target else 0
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = ((l + r) // 2)
        print(f"l: {l}, r: {r}, mid: {mid}")
        if nums[mid] == target:
            print(f"l: {l}, r: {r}, mid: {mid}")
            return mid
        elif nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        if nums[l] < nums[mid]:
            if nums[mid] > target and nums[l] <= target:
                r = mid - 1
            else:
                l = mid + 1  
        else:
            if nums[r] == target:
                return r
            l = mid + 1
        print(f"l: {l}, r: {r}, mid: {mid}")
    return -1

# print(search([4,5,6,7,0,1,2], 4))
print(search([5,1,2,3,4], 1))

    
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTracker(candidates: List[int], target: int, curr: List[int]):    
            if sum(curr) > target:
                return
            if sum(curr) == target:
                for i in res:
                    if self.checkDuplicate(i, curr):
                        return
                res.append(curr[:])
                return 
            for i in range(len(candidates)):
                curr.append(candidates[i])
                backTracker(candidates, target, curr)
                curr.pop()
        backTracker(candidates, target, [])
        return res

    def checkDuplicate(self, list1: List[int], list2: List[int]) -> bool:
        if len(list1) != len(list2):
            return False
        def list_to_map(lst: List[int]):
            hash_map = {}
            for i in lst:
                if i in hash_map:
                    hash_map[i] += 1
                else: 
                    hash_map[i] = 1
            return hash_map
        return list_to_map(list1) == list_to_map(list2)
            
    
sol = Solution()

# print(sol.combinationSum([2,3,6,7], 7))
# print(sol.combinationSum([2,3,5], 5))
# print(sol.combinationSum([2], 1))
print(sol.combinationSum([7,3,2], 18))

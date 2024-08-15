from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backTracker(candidates: List[int], target: int, curr: List[int]):    
            # print(curr)
            if sum(curr) > target:
                return
            if sum(curr) == target:
                res.append(curr)
                return 
            for i in range(len(candidates)):
                # print(candidates[i])
                curr.append(candidates[i])
                backTracker(candidates, target, curr)
                curr.pop()
        backTracker(candidates, target, [])
        return res

sol = Solution()

print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([2,3,5], 5))
print(sol.combinationSum([2], 1))
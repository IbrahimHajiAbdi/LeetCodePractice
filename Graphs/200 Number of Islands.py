from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        res = 0
        
        def dfs(y, x):
            if (y, x) in seen:
                return
            if grid[y][x] == "0":
                return
                
        
sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
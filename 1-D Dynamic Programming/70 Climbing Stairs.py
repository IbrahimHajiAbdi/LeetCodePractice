class Solution:
    def climbStairs(self, n: int) -> int:
        # if n < 0:
        #     return 0
        # if n == 0:
        #     return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        seen = {
            0: 1,
            1: 1,    
        } # no. of stairs : total unique combinations
        def recurse(n: int):
            if n in seen:
                return seen[n]
            if n < 0:
                return 0
            seen[n] = recurse(n-1) + recurse(n-2)
            print(len(seen))
            return seen[n]
        return recurse(n)
        
sol = Solution()
print(sol.climbStairs(45))
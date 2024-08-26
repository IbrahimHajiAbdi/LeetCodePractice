from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        seen = {} # index : no. solutions
        @cache
        def dp(i: int) -> int:
            # base cases
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in seen:
                return seen[i]

            if int(s[i:i+2]) <= 26 and i < len(s) - 1:
                seen[i] =  dp(i+1) + dp(i+2)
                return seen[i]
            seen[i] = dp(i+1)
            return seen[i]
        return dp(0)

sol = Solution()
print(sol.numDecodings("1111111111111111111111111111"))
from typing import List
from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        if len(coins) == 1:
            if amount % coins[0] != 0:
                return -1
            return amount // coins[0]
        seen = {} # amount : int

        def dp(remain: int) -> int:
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            if remain in seen:
                return seen[remain]

            res = float('inf')

            for coin in coins:
                seen[remain - coin] = dp(remain - coin)
                if seen[remain - coin] > 0:
                    res = min(seen[remain - coin] + 1, res)
            return 0 if res == float('inf') else res
        return dp(amount) - 1
    
sol = Solution()
print(sol.coinChange([1,2,5], 1000))
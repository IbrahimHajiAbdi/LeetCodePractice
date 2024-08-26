from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = {} # remaining string : if possible to break up -> bool
        def dfs(i: int, currStr: str) -> bool:
            # base cases:
            # if end of string and the currStr is empty meaning sucessfully decoded string
            # else didn't decode
            if i >= len(s):
                if currStr == "":
                    return True
                else:
                    return False
            if currStr in seen:
                return seen[currStr]
            currStr += s[i]
            # checks if the string is in wordDict than branches from that point
            # by continuing with currStr and starting a new string 
            if currStr in wordDict:
                seen[currStr] = dfs(i + 1, currStr) or dfs(i + 1, "")
                return seen[currStr]
            # currStr isn't in wordDict and isn't end of string, recurse further
            return dfs(i + 1, currStr)      
        return dfs(0, "")
    
sol  = Solution()
print(sol.wordBreak("catskicatcats", ["cats","cat","dog","ski"]))
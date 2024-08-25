from functools import cache

class Solution:
    @cache
    def longestPalindrome(self, s: str) -> str:
        seen = {} # string : bool
        res = ""
        if len(s) == 1:
            return s[0]
        if len(s) == 2:
            return s[0] if s[0] != s[1] else s

        def validPalindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True
        def longest(l: int, r: int, currMax: int):
            if l == r or (l, r) in seen or len(s[l:r+1]) < currMax:
                return
            seen[(l, r)] = validPalindrome(l, r)
            longest(l+1, r, currMax)
            for k, v in seen.items():
                if v and len(s[k[0]:k[1]+1]) > currMax:
                    currMax = len(s[k[0]:k[1]+1])
            longest(l, r-1, currMax)
        longest(0, len(s)-1, 1)
        
        
        for k, v in seen.items():
            if v and (k[1] - k[0] + 1) > len(res):
                res = s[k[0]:k[1]+1]
        print(len(seen))
        return s[0] if res == "" else res
    # def longestPalindrome(self, s: str) -> str:
    #     for i in range(len(s)):
            
    
sol = Solution()
# print(sol.longestPalindrome("boqylncwfahjzvawrojyhqiymirlkfzkhtvmbjnbfjxzewqqqcfnximdnrxtrbafkimcqvuprgrjetrecqkltforcudmbpofcxqdcirnaciggflvsialdjtjnbrayeguklcbdbkouodxbmhgtaonzqftkebopghypjzfyqutytbcfejhddcrinopynrprohpbllxvhitazsjeyymkqkwuzfenhphqfzlnhenldbigzmriikqkgzvszztmvylzhbfjoksyvfdkvshjzdleeylqwsapapduxrfbwskpnhvmagkolzlhakvfbvcewvdihqceecqhidvwecvbfvkahlzlokgamvhnpkswbfrxudpapaswqlyeeldzjhsvkdfvyskojfbhzlyvmtzzsvzgkqkiirmzgibdlnehnlzfqhphnefzuwkqkmyyejszatihvxllbphorprnyponircddhjefcbtytuqyfzjpyhgpobektfqznoatghmbxdouokbdbclkugeyarbnjtjdlaisvlfggicanricdqxcfopbmducroftlkqcertejrgrpuvqcmikfabrtxrndmixnfcqqqwezxjfbnjbmvthkzfklrimyiqhyjorwavzjhafwcnlyqob"))
print(sol.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"))
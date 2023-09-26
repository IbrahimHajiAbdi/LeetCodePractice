#!/bin/python3.10
def characterReplacement(s: str, k: int) -> int:
    res = 0
    initial_k = k
    for i in range(2):
        for l in range(len(s) - 1):
            r = l + 1
            count = 1
            char = s[l]
            k = initial_k
            while r < len(s):
                if s[r] == char:
                    count += 1
                elif k > 0:
                    k -= 1
                    count += 1
                else:
                    res = max(res, count)
                    break
                r += 1
                res = max(res, count)
        s = s[::-1]
    return res


string = "BAAAB"
print(characterReplacement(string, 2))

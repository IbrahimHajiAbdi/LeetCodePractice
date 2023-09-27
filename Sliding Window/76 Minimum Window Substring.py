#!/bin/python3.10

# r pointer goes increments until there is a valid substring, then l pointer increments until the string is invalid
# once the current substring is invalid, r pointer goes increments until it is valid again.
# Once r pointer reaches the end of the string, the l pointer increments toward the end of the string.
def minWindow(s: str, t: str) -> str:
    if t == s:
        return s
    count = {}
    t_count = {}
    substring = ""
    res = ""
    for char in t:
        t_count[char] = 1 + t_count.get(char, 0)

    def checkValidSubstring() -> bool:
        for k, v in t_count.items():
            if count.get(k, 0) > 0:
                if count.get(k) >= v:
                    continue
                else:
                    return False
            else:
                return False
        return True

    l = 0
    r = 0
    while r < len(s) and l < len(s):
        if checkValidSubstring():
            if res != "":
                if len(res) > len(substring):
                    res = substring
                count[s[l]] -= 1
                l += 1
                substring = substring[1:]
            else:
                res = substring
                count[s[l]] -= 1
                l += 1
                substring = substring[1:]
        else:
            count[s[r]] = 1 + count.get(s[r], 0)
            substring += s[r]
            r += 1
        if r >= len(s):
            while l < len(s):
                if checkValidSubstring():
                    if res != "":
                        if len(res) > len(substring):
                            res = substring
                    else:
                        res = substring
                count[s[l]] -= 1
                l += 1
                substring = substring[1:]
                print(f"Substring: {substring}\nres: {res}\n")
                print(f"l: {l}\nr: {r}\n")

        print(f"Substring: {substring}\nres: {res}\n")
        print(f"l: {l}\nr: {r}\n")
    return res



print(minWindow("ab", "b"))


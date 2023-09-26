def minWindow(s: str, t: str) -> str:
    count = {}
    t_count = {}
    res = ""
    for char in t:
        t_count[char] = 1 + t_count.get(char, 0)
    l = 0

    def tIns():
        for k, v in t_count.values():
            if count.get(k) is not None:
                if count.get(k) >= v:
                    continue
                else:
                    return False
            else:
                return False
        return True

    for r in range(len(s)):
        count[r] = 1 + count.get(count[r], 0)
        if tIns():
            if


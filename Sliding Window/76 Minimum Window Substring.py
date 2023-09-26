def minWindow(s: str, t: str) -> str:
    count = {}
    t_count = {}
    for char in t:
        t_count[char] = 1 + t_count.get(char, 0)
    l = 0
    for r in range(len(s)):


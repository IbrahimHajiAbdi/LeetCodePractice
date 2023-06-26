def lengthOfLongestSubstring(s):
  if len(set(s)) == 1:
    return 1
  substring = ""
  res = ""
  l, r, startPtr = 0, 1, 0
  while (r < len(s)):
    print(f"substring: {substring}\nleft ptr: {s[l]}\nright ptr: {s[r]}")
    if not substring and s[r] != s[l]:
      substring += s[l] + s[r]
    elif s[r] != s[l]:
      if s[r] not in substring:
        substring += s[r]
      else:
        if len(res) < len(substring):
          res = substring
        substring = ""
        s = s[1:]
        l = -1; r = 0
    else:
      substring = ""
    l += 1; r += 1
    if len(res) < len(substring):
      res = substring
    print("substring at end:", substring)
    print()
      
  return res

print(lengthOfLongestSubstring("dvdf"))
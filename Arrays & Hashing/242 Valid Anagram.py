def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    map1 = {}
    map2 = {}
    
    for i in s:
        if i not in map1:
            map1[i] = 1
        else:
            map1[i] += 1
    
    for i in t:
        if i not in map2:
            map2[i] = 1
        else:
            map2[i] += 1
    
    return map1 == map2

isAnagram("cat", "cat")

    
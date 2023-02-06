def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    map1 = getHashmapOfLetters(s)
    map2 = getHashmapOfLetters(t)
    
    return map1 == map2

def getHashmapOfLetters(s):
    map = {}
    for i in s:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1
    return map

isAnagram("cat", "cat")


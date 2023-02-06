def groupAnagrams(strs):
    ls = strs[:]
    ans = []
    
    for i in range(len(ls)):
        ls[i] = sorted(ls[i])
        
    for i in range(len(ls)):
        inAns = False
        for j in range(i, len(ls)):
            if ls[i] == ls[j]:
                
                
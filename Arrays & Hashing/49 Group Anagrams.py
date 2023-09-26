def groupAnagrams(strs):
    ls = {}
    
    for i in range(len(strs)):
        letters = [0 for i in range(26)]
        for j in range(strs[i]):
            
                
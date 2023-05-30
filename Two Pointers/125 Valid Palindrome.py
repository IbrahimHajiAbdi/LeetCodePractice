def isPalindrome(s):
    s = "".join(filter(str.isalnum, s))
    s = s.lower()
    if s == "": return True
    print(s)
    basePtr = 0
    endPtr = len(s)-1
    for i in range(len(s)//2):
        if s[basePtr+i] != s[endPtr-i]:
            return False
    return True 
    
print(isPalindrome("aaavv"))
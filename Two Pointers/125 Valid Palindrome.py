def isPalindrome(s):
    s = "".join(filter(str.isalnum, s))
    s = s.lower()
    if s == "": return True
    print(s)
    basePtr = 0
    endPtr = len(s)-1
    
    
isPalindrome("123aAAAAAAsd'#")
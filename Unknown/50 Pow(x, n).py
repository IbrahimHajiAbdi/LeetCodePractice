def myPow(x: float, n: int) -> float:
    if n >= 1:
        return x ** n
    elif n == 0:
        return 1
    else:
        return (1/x) ** -n
        
    
print(myPow(2, -2))
def multiply(num1: str, num2: str) -> str:
    num1_int = 0
    num2_int = 0
    for i in range(len(num1) - 1, -1, -1):
        print(num1_int, int(num1[i]) * 10 ** i)
        num1_int += int(num1[i]) * 10 ** (len(num1) - i - 1)
        
    for i in range(len(num2) - 1, -1, -1):
        num2_int += int(num2[i]) * 10 ** (len(num2) - i - 1)

    return str(num1_int*num2_int)

print(multiply("123", "456"))
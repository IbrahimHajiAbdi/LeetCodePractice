def multiply(num1: str, num2: str) -> str:
    num1_int = 0
    num2_int = 0
    for i in range(max(len(num1), len(num2)), 0, -1):
        num1_int += int(num1[i]) * 10 ** i
        num2_int += int(num2[i]) * 10 ** i
        print(num1_int, num2_int)

    return str(num1_int*num2_int)
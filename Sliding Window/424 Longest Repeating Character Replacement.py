#!/bin/python3.10
def characterReplacement(s, k):
    chars = set(s)
    res = 0
    initial_k_val = k
    for char in chars:
        count = 0
        ptr = 0
        k = initial_k_val
        while ptr < len(s):
            print(f"substring: {count}\nptr: {ptr}\n")
            if s[ptr] != char:
                if k > 0:
                    k -= 1
                    count += 1
                else:
                    count = 0
                    k = initial_k_val
            else:
                count += 1
            ptr += 1
            res = max(res, count)
    return res


def characterReplacement2(s, k):
    res = 0
    chars = set(s)
    chars_dict = {}

    for i, char in enumerate(s):
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    window_size = max(chars_dict.values()) + k
    l, r = 0, window_size - 1

    for i in range(len(s) - window_size + 1):

    return res


string = "SDSSMESS"
print(characterReplacement(string, 0))

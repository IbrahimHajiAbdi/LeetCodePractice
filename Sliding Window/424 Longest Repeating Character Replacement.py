def characterReplacement(s, k):
  chars = set(s)
  res = 0
  initial_k_val = k
  for char in chars:
    substring = ""
    ptr = 0
    k = initial_k_val
    while (ptr < len(s)):
      # print(f"substring: {substring}\nptr: {ptr}\n")
      if s[ptr] != char:
        if k > 0:
          k -= 1
          substring += char
        else: substring = ""
      else: substring += s[ptr]
      ptr += 1
      res = max(res, len(substring))
  return res

def characterReplacement2(s, k):
  chars = set(s)
  res = 0
  char_dict = {}
  
  for char in chars:
    ptr = 0
    char_dict[char] = ""
    while (ptr < len(s)):
      if s[ptr] == char:
        char_dict[char] += char
      else: char_dict[char] += "_"
      ptr += 1
  
  print(char_dict)
  
  return res
  
string = "AAKRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOFBABBA"
print(characterReplacement2(string, 4))

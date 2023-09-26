def containsDuplicate(nums):
    hash = {}
    hash_length = 0
    for i in range(len(nums)):
        if nums[i] in hash:
            return True
        else: 
            hash[hash_length] = nums[i]
            hash_length += 1
    print(hash)
    return False 

print(containsDuplicate([2,2]))

def productExceptSelf(nums):
    num_dict = {}
    for num in nums:
        if num in num_dict:
            num_dict[num] = num_dict[num] + 1
        else:
            num_dict[num] = 1 
    
    ans = []
    prod = 1
    for i in range(len(nums)):
        for key, value in num_dict.items():
            if nums[i] == key and value > 0:
                value = value - 1
            prod = prod * value * key
            print(prod)

productExceptSelf([1,2,3,4])

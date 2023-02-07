def productExceptSelf(nums):
    map = {}
    for i in range(len(nums)):
        map[nums[i]] = map.get(nums[i], 0) + 1
    

    print(map)


productExceptSelf([1,2,3,4])

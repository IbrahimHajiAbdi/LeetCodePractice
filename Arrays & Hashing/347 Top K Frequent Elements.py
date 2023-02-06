def topKFrequent(nums, k):
    if len(nums) <= 1:
        return nums
    map = {}
    for i in range(len(nums)):
        if nums[i] in map: 
            map[nums[i]] += 1
        else:
            map[nums[i]] = 1 
    
    map = [(v, k) for k, v in map.items()]; sorted(map)
    res = []
    for i in range(k):
        res.append(map[i][1])
    return res
    



print(topKFrequent([1,1,1,2,2,3], 2))
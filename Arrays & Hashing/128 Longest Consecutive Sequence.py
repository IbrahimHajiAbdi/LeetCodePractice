def longestConsecutive(nums):
    if len(nums) == 1: return 1
    elif len(nums) < 1: return 0
    num_set = set(nums)
    sorted_num_set = sorted(num_set)
    c = 1
    ans = 0
    for i in range(len(sorted_num_set)-1):
        if sorted_num_set[i] + 1 == sorted_num_set[i+1]:
            c += 1
        elif sorted_num_set[i] - 1 == sorted_num_set[i+1]:
            c += 1
        else:
            if c > ans: ans = c
            c = 1
    
    if len(sorted_num_set) == 1: return 1

    return ans if ans > c else c 

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
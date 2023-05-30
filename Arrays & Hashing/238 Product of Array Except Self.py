def productExceptSelf(nums):
    total = 1
    for i, num in enumerate(nums):
        total = total * num
    
    for i in range(len(nums)):
        
        
productExceptSelf([1,2,3,4])

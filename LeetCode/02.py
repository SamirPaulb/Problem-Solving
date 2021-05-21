nums = [-1,0,0,0,0,3,3]
i = 0
while i< len(nums)-1:
    if nums[i] == nums[i+1]:
        nums.pop(nums[i])
    else:
        i +=1


print(len(nums))

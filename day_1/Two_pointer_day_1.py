##### Two Sum Two Pointer

def two_pointer_two_sum(nums,target):
    left=0
    right=len(nums)-1
    while(left<right):
        if nums[left]+nums[right]>target:
            right-=1
        elif nums[left]+nums[right]<target:
            left+=1
        else:
            return [left,right]
    return -1
nums=[2,7,11,15,17,19]
target=36
print(two_pointer_two_sum(nums,target))
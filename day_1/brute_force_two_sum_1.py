##### Two Sum Brute Force

def brute_force_two_sum(nums,target):
    idx1,idx2=0,0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]

nums=[2,7,11,15,17]
target=17
print(brute_force_two_sum(nums,target))
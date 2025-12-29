######### Prefix Sum Range Sum Query

def prefix_sum_given_range(nums,left,right):
    N=len(nums)
    pf=[0]*(N+1)
    for i in range(N):
        pf[i+1] = pf[i] + nums[i]
    
    return pf[right+1]-pf[left]

nums =[-2, 0, 3, -5, 2, -1]
l=0
r=2
print(prefix_sum_given_range(nums,l,r))
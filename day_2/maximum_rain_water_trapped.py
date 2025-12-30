#### maximum Rain water trapped

def maximum_rain_water_trapped(nums):
    N=len(nums)
    prefix_max=[0]*N
    postfix_max=[0]*N
    
    prefix_max[0] = nums[0]
    postfix_max[N-1] = nums[N-1]
    
    for i in range(1,N):
        prefix_max[i] = max(prefix_max[i-1],nums[i])
        
    for i in range(N-2,-1,-1):
        postfix_max[i] = max(postfix_max[i+1],nums[i])
        
    max_rain_water_trapped=0
    
    for i in range(N):
        max_rain_water_trapped+= min(prefix_max[i],postfix_max[i]) -nums[i]
    
    return max_rain_water_trapped


heights=[0,1,0,2,1,0,1,3,2,1,5,9]

print(maximum_rain_water_trapped(heights))

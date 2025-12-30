##### Maximum product of Sub Array 

def maximum_product_of_sub_array(nums):
    N=len(nums)
    Prefix=[0]*N
    Postfix=[0]*N
    
    Prefix[0] = nums[0]
    Postfix[N-1] = nums[N-1]
    
    for i in range(1,N):
        Prefix[i] = Prefix[i-1]*nums[i]
    
    for i in range(N-2,-1,-1):
        Postfix[i] = Postfix[i+1] * nums[i]
        
    maximumMultipled = max(Prefix[0],Postfix[0])
    
    for i in range(1,N):
        maximumMultipled = max(Prefix[i],maximumMultipled,Postfix[i])
    
    return maximumMultipled

array = [2,3,-2,4]

print(maximum_product_of_sub_array(array))

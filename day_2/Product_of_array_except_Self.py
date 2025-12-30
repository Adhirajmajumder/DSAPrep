############# Product Of Array Except Self 
#def product_of_array(nums):
#    N=len(nums)
#    PreFix = [1]*N
#    PostFix = [1]*N
#    
#    for i in range(1,N):
#        PreFix[i] =PreFix[i-1]* nums[i-1]
#        
#    for i in range(N-1,-1,-1):
#        PostFix[i-1] =PostFix[i]* nums[i]
#    PostFix[N-1]=1
#    for i in range(N):
#        PreFix[i]=PostFix[i]*PreFix[i]
#    return PreFix,PostFix

def optimized_array_multiplication(nums):
    N=len(nums)
    answer=[1]*N
    right=1
    for i in range(1,N):
        answer[i]=answer[i-1]*nums[i-1]
    for i in range(N-1,-1,-1):
        right*=nums[i]
        answer[i-1]*=right
    return answer
array = [2, 3, 4, 5]
print(optimized_array_multiplication(array))
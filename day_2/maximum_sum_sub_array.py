###################### Maximum Sub Array
def Maximum_sub_array(nums):
    N=len(nums)
    max_sum=-float('inf')
    current_sum=-float('inf')
    answer=[]
    for i in range(N):
        current_sum = max(nums[i], current_sum+nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
array = [-5, -2, -8]
print(Maximum_sub_array(array))
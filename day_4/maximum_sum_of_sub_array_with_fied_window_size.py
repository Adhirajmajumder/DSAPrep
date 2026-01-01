##### Maximum sum of sub array with size k

def maximum_sum_subarray_with_fixed_window_size(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum 
    
    for r in range(k,len(nums)):
        l=r-k
        window_sum += nums[r]
        window_sum -= nums[l]
        max_sum = max(window_sum,max_sum)
    return max_sum
array = [2, 3, 5, -2, 7, -4]

print(maximum_sum_subarray_with_fixed_window_size(array,3))
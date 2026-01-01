###### Minimum Size of subarray sum

def minimum_size_subarray_sub(nums,target):
    l=0
    min_length=float('inf')
    answer=0
    for r in range(len(nums)):
        answer += nums[r]
        
        while answer>=target:
            print(r,l,answer,min_length)
            min_length = min(min_length,r-l+1)
            answer -= nums[l]
            l+=1
        
    return min_length if min_length != float('inf') else 0
array = [1, 4, 45, 6, 20, 5]
print(minimum_size_subarray_sub(array,26))
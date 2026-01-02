##### Sub Array sum equals K ####

def sub_array_sum_equals_k(array,k):
    prefix_sum = 0
    freq={0:1}
    count=0
    
    for num in array:
        prefix_sum += num
        
        if prefix_sum-k in freq:
            count += freq[prefix_sum-k]
        
        freq[prefix_sum] = freq.get(prefix_sum,0)+1
    return count

array = [3,4,7,2,-3,1,4,2]
print(sub_array_sum_equals_k(array,7))
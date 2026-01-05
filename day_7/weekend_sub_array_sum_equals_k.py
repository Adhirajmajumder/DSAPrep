##### Sub Array sum equals K #####
def sub_array_sum_equals_k(array,k):
    hash_map={0:1}
    count = 0
    prefix_sum=0
    for val in array:
        prefix_sum+=val
        
        if prefix_sum-k in hash_map:
            count +=  hash_map[prefix_sum-k]
        hash_map[prefix_sum] = hash_map.get(prefix_sum,0) + 1
    
    return count
array = [10, 2, -2, -20, 10]
print(sub_array_sum_equals_k(array,-10))
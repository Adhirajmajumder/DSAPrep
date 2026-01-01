############## Top K Frequenct Element ##################
def top_k_frequent_element(array,k):
    hash_map = {}
    grouped_count=[[] for _ in range(len(array))]
    answer=[]
    
    for i in array:
        hash_map[i] = hash_map.get(i,0) + 1
    
    for num,count in hash_map.items():
        grouped_count[count].append(num)
    
    for num in range(len(grouped_count)-1,0,-1):
        for i in grouped_count[num]:
            answer.append(i)
            if i==k:
                return answer

nums=[1,2,1,2,1,2,3,1,3,2,5,2,5,6,9,5,6]
print(top_k_frequent_element(nums,5))
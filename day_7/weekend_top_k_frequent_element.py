#### Top K frequent element ######

def top_k_frequent_element(array,k):
    hash_map={}
    bucket=[[] for _ in range(len(array))]
    answer=[]
    for val in array:
        hash_map[val] = hash_map.get(val,0) + 1
        
    for val, freq in hash_map.items():
        bucket[freq].append(val)
    
    for value in range(len(bucket)-1,0,-1):
        for i in bucket[value]:
            answer.append(i)
            if len(answer)==k:
                return answer
array =[1,1,2,2,4,3,3,5,5,5,7,8]
print(top_k_frequent_element(array,4))
        
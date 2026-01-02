######## Top K frequenct elements #############

def top_k_frequent_element(array,k):
    hash_map={}
    bucket=[[] for _ in range(len(array)+1)]
    answer=[]
    
    for i in array:
        hash_map[i] = hash_map.get(i,0) + 1
    
    for num,freq in hash_map.items():
        bucket[freq].append(num)
    
    for i in range(len(bucket)-1,0,-1):
        for num in bucket[i]:
            answer.append(num)
            if len(answer) == k:
                return answer,bucket

array = [1,1,1,2,2,3,3,4,4,4,4]
print(top_k_frequent_element(array,3))
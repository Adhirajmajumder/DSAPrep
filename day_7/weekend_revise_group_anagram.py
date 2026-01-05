#### Group Anagram #####
#from collections import defaultdict

#def group_anagram(array):
#    hash_map=defaultdict(list)
#    
#    for strs in array:
#        val = ''.join(sorted(strs))
#        hash_map[val].append(strs)
#    
#    return list(hash_map.values())
#    
#array =["tan","net","ate","aet","bat","ten","ent"]
#print(group_anagram(array)) ## compleixty O(N)* (KLogN)


def optimized_group_anagram(array):
    hash_map={}
    for strs in array:
        count = [0] * 26
        for char in strs:
            count[ord(char)-ord('a')] += 1
        
        count_tuple = tuple(count)
        if count_tuple not in hash_map: 
            hash_map[count_tuple]=[]
        
        hash_map[count_tuple].append(strs)
    
    return list(hash_map.values())

array =["tan","net","ate","aet","bat","ten","ent"]
print(optimized_group_anagram(array)) ## compleixty O(N)* (K(26)) O(N)

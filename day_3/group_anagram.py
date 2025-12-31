########## Group Anagram ###############
#from collections import defaultdict

#def group_anagram_by_sorting(strs):
#    anagram_hash={}
#    
#    for word in strs:
#        sorted_word = ''.join(sorted(word))
#        if sorted_word not in anagram_hash:
#            anagram_hash[sorted_word] = []
#        anagram_hash[sorted_word].append(word)
#    
#    return list(anagram_hash.values())
#    
#strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
#print(group_anagram_by_sorting(strs))

def group_anagram_by_counting(strs):
    anagram_hash={}
    
    for word in strs:
        
        count=[0]*26
        for char in word:
            count[ord(char)-ord('a')] += 1
        
        counting_tuple = tuple(count)
        if counting_tuple not in anagram_hash:
            anagram_hash[counting_tuple] =[]
        anagram_hash[counting_tuple].append(word)
    
    return list(anagram_hash.values())
    
    
strs = ["eat","tea","tan","bat","nat","ate","cat","rat"]

print(group_anagram_by_counting(strs))
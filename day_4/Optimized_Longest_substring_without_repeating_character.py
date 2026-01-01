####### Longest Substring Array without Duplicate

def Longest_Substring_subarray_without_duplicate_optimied(strs):
    hash_map={}
    l=0
    maxLength = 0
    for r,ch in enumerate(strs):
        if ch in hash_map and hash_map[ch] >= l:
            l=hash_map[ch]+1
            del hash_map[ch]
        hash_map[ch]=r
        maxLength=max(maxLength,r-l+1)
    return maxLength,hash_map.keys()

strs="pwwkew"

print(Longest_Substring_subarray_without_duplicate_optimied(strs))
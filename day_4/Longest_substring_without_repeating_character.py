######### Longest Subtring Without repetating character

def longest_substring_without_repeating_character(strs):
    l=0
    
    output=list()
    maxLen=0
    for r in range(len(strs)):
        
        print(output)
        while strs[r] in output:
            output.remove(strs[l])
            l+=1
        output.append(strs[r])
        maxLen=max(maxLen,r-l+1)
    return ''.join(output),maxLen

strs="abcabcb"
print(longest_substring_without_repeating_character(strs))
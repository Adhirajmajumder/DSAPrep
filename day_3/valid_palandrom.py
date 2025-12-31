####### Valid Palindrom
from copy import deepcopy
def valid_palindrom(strs):
    left=0
    right=len(strs)-1
    string_check=deepcopy(strs)
    while(left<right):
        strs[left],strs[right]=strs[right],strs[left]
        left+=1
        right-=1
     
    return string_check==strs #,strs,string_check

#strs=list("gurdian")
#strs=list("madam")
strs=list("malayalam")
print(valid_palindrom(strs))
    

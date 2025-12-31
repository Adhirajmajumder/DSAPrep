####### Leetcode Blind 75 Valid Anagram ##############

def valid_anagram(s,t):
    dictS,dictT = {},{}
    
    for c in s:
        dictS[c] = dictS.get(c,0)+1
    for c in t :
        dictT[c] = dictT.get(c,0)+1
    return dictS==dictT

s="MADAM"
t="MADAM"
#s="DOG"
#t="GOD"
#s="MALAYLAYAM"
#t="MALAYLAYAM"
 
print(valid_anagram(s,t))
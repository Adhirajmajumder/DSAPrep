#### Reverse A String ####

#def reverse_string(s):
#    if len(s)<=1:
#        return s[0]
#    
#    return reverse_string(s[1:])+s[0]
#
#strings = "Dictionary"
#print(reverse_string(strings))

def optimized_reverse_string_recursive(strings,i=0):
    if i==len(strings):
        return ""
    
    return optimized_reverse_string_recursive(strings,i+1) + strings[i]


strings = "I love coding"
print(optimized_reverse_string_recursive(strings))
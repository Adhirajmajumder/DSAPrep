### Palidrom Check ###

### Paplindrom check using Recursion ###

def palindrom_check_using_recursion(array,left,right):
    if left>=right:
        return True
    
    if array[left]!=array[right]:
        return False
    
    return palindrom_check_using_recursion(array,left+1,right-1)

#strings="adhiraj"
strings="malayalam"
print(palindrom_check_using_recursion(strings,0,len(strings)-1))
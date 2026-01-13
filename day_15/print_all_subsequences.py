#### Print All subsequences ###

def print_all_subsequences(array, index, current):
    if len(array)==index:
        print(current)
        return 
    
    print_all_subsequences(array, index+1, current + array[index])
    
    print_all_subsequences(array, index+1, current)
    

print_all_subsequences("abcde", 0, "")
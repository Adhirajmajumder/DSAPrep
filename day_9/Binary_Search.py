#### Binary Search ####

def binary_search(array,target):
    right=len(array)
    mid=0
    left=0
    
    while(left<right):
        mid=(left+right)//2
        if array[mid]<target:
            left+=1
        elif array[mid]>target:
            right-=1
        elif array[mid]==target:
            return mid+1
    return -1

array = [1,3,5,7,9]
print(binary_search(array,7))
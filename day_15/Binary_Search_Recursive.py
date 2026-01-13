### Binary Search Recusive way ###

def binary_search_recursive(array, low,high,target):
    if array is None:
        return -1
    
    if low>high:
        return -1
    
    mid = (low+high)//2
    
    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search_recursive(array, low,mid-1,target)
    else:
        return binary_search_recursive(array, mid+1, high, target)

array = [-4,-3,-2,-1,0,1,2,3,4,5,6,7,8]
print(binary_search_recursive(array,0,len(array)-1,7))
### Find Minimum in Rotated Sorted Array ###

def find_minimum_in_rotated_sorted_array(array):
    left,right=0,len(array)-1
    
    while left<right:
        mid=(right+left)//2
        
        if array[right]<array[mid]:
            left=mid+1
        else:
            right=mid
            
    return array[left]
    
array = [4,5,6,7,-1,0,1,2,3]
print(find_minimum_in_rotated_sorted_array(array))
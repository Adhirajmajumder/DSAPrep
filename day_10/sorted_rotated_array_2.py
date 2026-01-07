#### Binary search of sorted rotated array ####

def sorted_rotated_array(array,target):
    left,right = 0,len(array)-1
    
    while(left<=right):
        mid=(left+right)//2
        
        if array[mid]==target:
            return mid+1
        
        if array[left]<=array[mid]:
            if array[left]<=target<target:
                right-=1
            else:
                left+=1
        else:
            if array[mid]<target<=target:
                l+=1
            else:
                r-=1
    return -1
    
    
array = [4,5,6,7,0,1,2]
target=0
print(sorted_rotated_array(array,target))
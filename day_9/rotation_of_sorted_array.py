### Rotated Sorted Array ###

def rotated_sorted_array(array, target):
    left,right=0,len(array)-1
    
    while left<=right:
        mid=(left+right)//2
        
        if array[mid]==target:
            return mid+1
        if array[left]<=array[mid]:
            if array[left]<=target<array[mid]:
                righrt-=1
            else:
                right+=1
        else:
            if array[mid]<target<=array[right]:
                left+=1
            else:
                right-=1
    return -1
array = [4,5,6,7,0,1,2]
target=0
print(rotated_sorted_array(array,target))
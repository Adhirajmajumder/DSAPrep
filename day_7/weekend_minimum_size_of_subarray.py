###### Minimum size of subarray #########

def minimum_size_subarray(array,target):
    left=0
    sums=0
    minLength=float('inf')
    for right in range(len(array)):
        sums += array[right]
        
        while sums>=target :
            sums -= array[left]
            minLength=min(minLength,right-left+1)
            left+=1
        #print(array[right],array[left])
    return minLength

#array = [2,3,1,2,4,3]
#array=[2, 3, 5, 2, 8,11]
array =[1,4,45,6,20,5]
print(minimum_size_subarray(array,7))
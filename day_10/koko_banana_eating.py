### Koko Banana eating ###

from math import ceil
def koko_banana_eating(array,target):
    low,high=1,max(array)
    
    while low<high:
        mid=(low+high)//2
        
        hours=0
        for i in array:
            hours+=ceil(i//mid)
        
        if hours<=target:
            high=mid
        else:
            low=mid+1
    return low
piles = [3,6,7,11]
h = 8

print(koko_banana_eating(piles,h))

        
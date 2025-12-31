########## Container with most water ###############

def container_with_most_water(nums):
    N=len(nums)
    left=0
    right=N-1
    maximum_water=0
    minimumHeight=0
    while(left<right):
        width=right-left
        minimumHeight = min(nums[left],nums[right])
        maximum_water = max(maximum_water,minimumHeight*width)
        
        if nums[left]<nums[right]:
            left+=1
        else:
            right-=1
    return maximum_water

array = [1,8,6,2,5,4,8,3,6]
print(container_with_most_water(array))
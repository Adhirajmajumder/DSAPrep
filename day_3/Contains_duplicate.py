############### Contains Duplicate ##############

def contains_duplicate(nums):
    answer=[]
    for i in range(len(nums)):
        if nums[i] in answer:
            return True
        answer.append(nums[i])
    return False
#nums=[1,2,3,4,1]
nums=[1,2,3,4,5]
print(contains_duplicate(nums))
### Sum Of Digits ###

def sum_of_digit(nums):
    if nums==0:
        return 0
    
    return (nums%10) + sum_of_digit(nums//10)

vals = 190051
print(sum_of_digit(vals))
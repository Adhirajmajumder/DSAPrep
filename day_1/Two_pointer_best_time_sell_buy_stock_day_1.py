############ Brute Force Best Time Sell and Buy Stock
def two_pointer_best_time_sell_buy_stock(nums):
    left=0
    right=1
    maxProfit=0
    N=len(nums)-1
    while(left<right and right<=N):
        current_profit = nums[right]-nums[left]
        #print(current_profit,maxProfit,nums[left],nums[right])
        if nums[right]>nums[left] :
            maxProfit = max(maxProfit,nums[right]-nums[left])
        elif nums[right]<nums[left]:
            left+=1
        right+=1
    return maxProfit
nums = [7, 1, 5, 3, 6, 4,10]


print(two_pointer_best_time_sell_buy_stock(nums))
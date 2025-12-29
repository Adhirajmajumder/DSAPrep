############ Brute Force Best Time Sell and Buy Stock
def brute_force_best_time_sell_buy_stock(nums):
    maxProfit=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            maxProfit=max(maxProfit, nums[j]-nums[i])
            #print(maxProfit)
    return maxProfit

prices = [7, 1, 5, 3, 6, 4]
print(brute_force_best_time_sell_buy_stock(prices))
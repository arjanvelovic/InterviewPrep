# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Use of dynamic window technique
def maxProfit(prices):
        maxprofit = 0
        currentprofit = 0
        windowStart = 0

        for windowEnd in range(len(prices)):
            currentprofit = prices[windowEnd] - prices[windowStart]
            maxprofit = max(maxprofit, currentprofit)

            while currentprofit < 0:
                windowStart += 1
                currentprofit = prices[windowEnd] - prices[windowStart]

        return maxprofit

print(maxProfit(prices=[7,1,5,3,6,4]))
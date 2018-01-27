__author__ = 'rishabh anand'




def coinChange(coins, amount):
    minTotal = [float('inf')] * (amount + 1)
    minTotal[0] = 0
    for coin in coins:
        for i in range(amount + 1):
            if i >= coin:
                minTotal[i] = min(minTotal[i], 1 + minTotal[i - coin])
    if minTotal[-1] == float('inf'):
        return -1
    return minTotal[-1]


print coinChange([1, 2, 5], 11)
print coinChange([2], 3)
print coinChange([186, 419, 83, 408], 6249)


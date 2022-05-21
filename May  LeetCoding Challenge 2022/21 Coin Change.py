#You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
#Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
#You may assume that you have an infinite number of each kind of coin.
#
# 
#
#Example 1:
#
#Input: coins = [1,2,5], amount = 11
#Output: 3
#Explanation: 11 = 5 + 5 + 1
#Example 2:
#
#Input: coins = [2], amount = 3
#Output: -1
#Example 3:
#
#Input: coins = [1], amount = 0
#Output: 0

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        rs = [amount+1] * (amount+1)
        rs[0] = 0
        for i in xrange(1, amount+1):
            for c in coins:
                if i >= c:
                    rs[i] = min(rs[i], rs[i-c] + 1)

        if rs[amount] == amount+1:
            return -1
        return rs[amount]
        
class Solution(object):
    def __init__(self):
        self.mem = {0: 0}
    
    def coinChange(self, coins, amount):
        coins.sort()
        minCoins = self.getMinCoins(coins, amount)
        
        if minCoins == float('inf'):
            return -1
        
        return minCoins
        
    def getMinCoins(self, coins, amount):
        if amount in self.mem:
            return self.mem[amount]
        
        minCoins = float('inf')
        
        for c in coins:
            if amount - c <  0:
                break
				
            numCoins = self.getMinCoins(coins, amount - c) + 1
            minCoins = min(numCoins, minCoins)
        
        self.mem[amount] = minCoins
        
        return minCoins
##Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
##Return the maximum product you can get.

##Example 1:
##Input: n = 2
##Output: 1
##Explanation: 2 = 1 + 1, 1 × 1 = 1.

##Example 2:
##Input: n = 10
##Output: 36
##Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1

        div = int(n / 3) 
        mod = n % 3
        if mod == 2:
            return 3**div * mod
        elif mod == 1:
            return 3**(div-1) * 2 * 2
        else:
            return 3**div
            
class Solution:
    def integerBreak(self, n: int) -> int:
        # Initialize dp array with 0's
        dp = [0]*(n+1)
        
        # Base case
        dp[2] = 1
        
        # Iterate from 3 to n
        for i in range(3, n+1):
            # Iterate from 1 to i//2
            for j in range(1, i//2+1):
                # Calculate the product of j and i-j
                prod = j*(i-j)
                
                # Update the maximum product in dp[i]
                dp[i] = max(dp[i], max(prod, j*dp[i-j]))
        
        # Return dp[n]
        return dp[n]
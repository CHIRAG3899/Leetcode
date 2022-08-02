##There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., ##grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The ##robot can only move either down or right at any point in time.
##Given the two integers m and n, return the number of possible unique paths that the robot can ##take to reach the bottom-right corner.
##The test cases are generated so that the answer will be less than or equal to 2 * 109.
##
##Example 1:
##Input: m = 3, n = 7
##Output: 28
##Example 2:
##Input: m = 3, n = 2
##Output: 3
##Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right ##corner:
##1. Right -> Down -> Down
##2. Down -> Down -> Right
##3. Down -> Right -> Down

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j-1]+aux[i-1][j]
        return aux[-1][-1]
		
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # -----------------------------------
        # key: (m, n) size of grid
        # value: total path count from source to destinaion
        memo = {}
        def path_count(m, n):
            if (m, n) in memo:   
                # look-up in memo
                return memo[(m, n)]
            if m == 0 or n == 0:    
                # base case
                memo[(m, n)] = 0
                return 0
            elif m == 1 and n == 1:    
                # base case
                memo[(m, n)] = 1
                return 1

            # general case
            memo[(m, n)] = path_count(m-1, n) + path_count(m, n-1)
            return memo[(m, n)]

        return path_count(m, n)
#You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.
#
#An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
#
#Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
#The testcases are generated so that the answer will be less than or equal to 2 * 109.
#
# 
#
#Example 1:
#
#
#Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
#Output: 2
#Explanation: There is one obstacle in the middle of the 3x3 grid above.
#There are two ways to reach the bottom-right corner:
#1. Right -> Right -> Down -> Down
#2. Down -> Down -> Right -> Right
#Example 2:
#
#
#Input: obstacleGrid = [[0,1],[0,0]]
#Output: 1

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]
        
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def rec(grid, i, j, d):
            if i > len(grid)-1 or j > len(grid[0])-1:
                return 0
            if grid[i][j] == 1:
                return 0
            if i == len(grid)-1 and j == len(grid[0])-1:
                return 1
            if (i,j) in d:
                return d[(i,j)]
            
            down = rec(grid, i+1, j, d)
            right = rec(grid, i, j+1, d)
            
            d[(i,j)] = down + right
            return d[(i,j)]
            
        return rec(obstacleGrid, 0, 0, {})
        
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0
        
        mem = dict()
        return self.findPaths(0, 0, obstacleGrid, mem)
    
    
    
    def findPaths(self, i, j, grid, mem):
        if (i,j) in mem:
            return mem[(i,j)]
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return 1
        
        c = 0
        for x, y in [(i+1,j), (i, j+1)]:
            if x < len(grid) and y < len(grid[0]) and not grid[x][y]:
                c += self.findPaths(x, y, grid, mem)
        
        mem[(i,j)] = c
        return c
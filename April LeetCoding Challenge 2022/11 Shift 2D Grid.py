#Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
#
#In one shift operation:
#
#Element at grid[i][j] moves to grid[i][j + 1].
#Element at grid[i][n - 1] moves to grid[i + 1][0].
#Element at grid[m - 1][n - 1] moves to grid[0][0].
#Return the 2D grid after applying shift operation k times.
#
# 
#
#Example 1:
#
#
#Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
#Output: [[9,1,2],[3,4,5],[6,7,8]]
#Example 2:
#
#
#Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
#Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
#Example 3:
#
#Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
#Output: [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def shiftGrid(self, grid, k):
        
        m=len(grid)# row in grid
        n=len(grid[0])# column in grid
        t=1
        
        while(t<=k):
           
            first=grid[0][0]
            for i in range(m):
                
                              
                for j in range(n):
                        
                        if i==0 and j==0:
                            continue
                        
                        else:
                            temp=grid[i][j]
                            grid[i][j]=first
                            first=temp
            grid[0][0]=first
            t=t+1    
        return grid

import numpy as np
class Solution(object):
    def shiftGrid(self, grid, k):
        grid = np.array(grid)           # convert into a numpy array
        ROW, COL = grid.shape           # Get Rows and Cols
        grid = grid.flatten()           # convert into 1-d
        grid = np.roll(grid,k)          # shift to k positions
        grid = grid.reshape((ROW,COL))  # reshape to original
        grid = grid.tolist()            # convert back to list
        return grid
        
class Solution(object):
    def shiftGrid(self, grid, k):
        l, m, n, k = [num for row in grid for num in row], len(grid), len(grid[0]), k % (len(grid) * len(grid[0]))  # grid to list
        l = l[-k:] + l[:-k]  # shift k times
        return [l[i * n: i * n + n] for i in range(m)]  # list to grid